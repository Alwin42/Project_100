from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Car, Profile, Rental, PaymentSettings
from .serializers import CarSerializer, RentalSerializer, PaymentQRSerializer
from .utils import generate_otp, send_otp_email

# --- PUBLIC CAR API ---
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # This allows ANYONE to see cars (GET), but only Logged-in users to Edit/Delete
    permission_classes = [IsAuthenticatedOrReadOnly] 

# --- AUTH VIEWS ---

@api_view(['POST'])
@permission_classes([AllowAny])
def auth_send_otp(request):
    """
    Takes an email. Creates a user if they don't exist. Sends OTP.
    """
    email = request.data.get('email')
    if not email:
        return Response({"error": "Email is required"}, status=400)

    # 1. Get or Create the User (Username = Email)
    user, created = User.objects.get_or_create(username=email, defaults={'email': email})
    
    if created:
        user.set_unusable_password() # We don't use passwords
        user.save()
        # Create the profile backpack
        if not hasattr(user, 'profile'):
            Profile.objects.create(user=user)

    # 2. Ensure Profile exists (just in case)
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)

    # 3. Generate and Save OTP
    otp = generate_otp()
    user.profile.otp = otp
    user.profile.otp_created_at = timezone.now()
    user.profile.save()

    # 4. Send Email
    try:
        send_otp_email(email, otp)
        return Response({"message": "OTP sent successfully!"})
    except Exception as e:
        print(f"Email Error: {e}") # Print error to console for debugging
        return Response({"error": "Failed to send email"}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
def auth_verify_otp(request):
    email = request.data.get('email')
    submitted_otp = request.data.get('otp')

    try:
        user = User.objects.get(email=email)
        profile = user.profile
        
        # Clean data
        clean_submitted = str(submitted_otp).strip()
        clean_stored = str(profile.otp).strip()
        
        # Verify OTP
        if clean_stored == clean_submitted and profile.is_otp_valid():
            
            # 1. Clear OTP (Security)
            profile.otp = None
            profile.save()
            
            # 2. GENERATE TOKEN (The "Key")
            token, _ = Token.objects.get_or_create(user=user)
            
            return Response({
                "message": "Login Successful", 
                "user_id": user.id,
                "email": user.email,
                "token": token.key
            })
        else:
            return Response({"error": "Invalid or Expired OTP"}, status=400)
            
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # User must be logged in
@parser_classes([MultiPartParser, FormParser]) # To handle image uploads
def upload_id_proof(request):
    user = request.user
    profile = user.profile
    
    # Get the image from the request
    image = request.FILES.get('id_proof')
    
    if not image:
        return Response({"error": "No image provided"}, status=400)
    
    # Save it
    profile.id_proof = image
    profile.save()
    
    return Response({"message": "ID Proof uploaded! Waiting for Admin approval."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_verification_status(request):
    profile = request.user.profile
    return Response({
        "is_verified": profile.is_verified,
        "has_uploaded_id": bool(profile.id_proof)
    })

# --- PAYMENT & RENTAL VIEWS ---

@api_view(['GET'])
@permission_classes([AllowAny]) # Anyone can see the QR to pay
def get_payment_qr(request):
    """
    Returns the Admin's UPI QR Code and ID.
    """
    settings = PaymentSettings.objects.first()
    if settings:
        serializer = PaymentQRSerializer(settings)
        return Response(serializer.data)
    return Response({"error": "No QR code configured"}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_rental(request):
    """
    Creates a new Rental record when user confirms payment.
    """
    user = request.user
    car_id = request.data.get('car_id')
    
    try:
        car = Car.objects.get(id=car_id)
        
        # Default: 1 Day Rental starting Today
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=1)
        
        # Create Record
        rental = Rental.objects.create(
            car=car,
            user=user,
            start_date=start_date,
            end_date=end_date,
            total_price=car.price_per_day, 
            status='Confirmed' # Assume payment success via UPI
        )
        
        # Mark car as unavailable so others can't rent it
        car.is_available = False
        car.save()
        
        return Response({"message": "Booking Confirmed!", "rental_id": rental.id})
        
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_rentals(request):
    """
    Returns the list of cars rented by the current user.
    """
    # Fetch rentals for THIS user, ordered by newest first
    rentals = Rental.objects.filter(user=request.user).order_by('-booked_at')
    serializer = RentalSerializer(rentals, many=True)
    return Response(serializer.data)