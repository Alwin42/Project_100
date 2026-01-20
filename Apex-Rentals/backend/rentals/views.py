from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Car, Profile, Rental
from .serializers import CarSerializer, RentalSerializer
from .utils import generate_otp, send_otp_email

# --- PUBLIC CAR API ---
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 

# --- AUTH VIEWS ---
@api_view(['POST'])
@permission_classes([AllowAny])
def auth_send_otp(request):
    email = request.data.get('email')
    if not email: return Response({"error": "Email is required"}, status=400)
    
    user, created = User.objects.get_or_create(username=email, defaults={'email': email})
    if created:
        user.set_unusable_password()
        user.save()
        if not hasattr(user, 'profile'): Profile.objects.create(user=user)
    
    if not hasattr(user, 'profile'): Profile.objects.create(user=user)

    otp = generate_otp()
    user.profile.otp = otp
    user.profile.otp_created_at = timezone.now()
    user.profile.save()

    try:
        send_otp_email(email, otp)
        return Response({"message": "OTP sent!"})
    except:
        return Response({"error": "Email failed"}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
def auth_verify_otp(request):
    email = request.data.get('email')
    submitted_otp = request.data.get('otp')
    try:
        user = User.objects.get(email=email)
        profile = user.profile
        if str(profile.otp).strip() == str(submitted_otp).strip() and profile.is_otp_valid():
            profile.otp = None
            profile.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "Login Success", "user_id": user.id, "email": user.email, "token": token.key})
        else:
            return Response({"error": "Invalid OTP"}, status=400)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def upload_id_proof(request):
    image = request.FILES.get('id_proof')
    if not image: return Response({"error": "No image"}, status=400)
    
    request.user.profile.id_proof = image
    request.user.profile.save()
    return Response({"message": "ID Uploaded"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_verification_status(request):
    return Response({"is_verified": request.user.profile.is_verified, "has_uploaded_id": bool(request.user.profile.id_proof)})

# --- RENTAL VIEWS ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser]) # Enable file upload
def create_rental(request):
    user = request.user
    car_id = request.data.get('car_id')
    payment_proof = request.FILES.get('payment_proof') # Get image

    if not payment_proof:
        return Response({"error": "Payment screenshot required"}, status=400)

    try:
        car = Car.objects.get(id=car_id)
        start_date = timezone.now().date()
        end_date = start_date + timedelta(days=1)
        
        rental = Rental.objects.create(
            car=car, user=user, start_date=start_date, end_date=end_date,
            total_price=car.price_per_day,
            payment_proof=payment_proof, # Save Image
            status='Pending Approval'
        )
        
        car.is_available = False
        car.save()
        return Response({"message": "Booking Submitted", "rental_id": rental.id})
        
    except Car.DoesNotExist:
        return Response({"error": "Car not found"}, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_rentals(request):
    rentals = Rental.objects.filter(user=request.user).order_by('-booked_at')
    serializer = RentalSerializer(rentals, many=True)
    return Response(serializer.data)