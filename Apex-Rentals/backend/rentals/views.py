from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Car, Profile
from .serializers import CarSerializer
from .utils import generate_otp, send_otp_email

# CarViewSet
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# ---  AUTH VIEWS ---

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
        print(e) # Print error to console for debugging
        return Response({"error": "Failed to send email"}, status=500)

@api_view(['POST'])
@permission_classes([AllowAny])
def auth_verify_otp(request):
    email = request.data.get('email')
    submitted_otp = request.data.get('otp')

    print("\n--- DEBUGGING LOGIN ---")
    print(f"1. Client Email: {email}")
    print(f"2. Client OTP: {submitted_otp}")

    try:
        user = User.objects.get(email=email)
        profile = user.profile
        
        # Clean the data
        clean_submitted = str(submitted_otp).strip()
        clean_stored = str(profile.otp).strip()
        
        print(f"3. Stored OTP (DB): '{clean_stored}'")
        print(f"4. Submitted OTP  : '{clean_submitted}'")
        
        # Check MATCH
        is_match = (clean_stored == clean_submitted)
        print(f"5. Do they match? {is_match}")
        
        # Check TIME
        is_time_valid = profile.is_otp_valid()
        print(f"6. Is time valid? {is_time_valid}")
        
        if not is_time_valid:
            # Print timing details if it failed
            from django.utils import timezone
            now = timezone.now()
            print(f"   -> Created At: {profile.otp_created_at}")
            print(f"   -> Current Time: {now}")
            print(f"   -> Difference: {now - profile.otp_created_at if profile.otp_created_at else 'None'}")

        if is_match and is_time_valid:
            print("--- LOGIN SUCCESS ---\n")
            profile.otp = None
            profile.save()
            return Response({
                "message": "Login Successful", 
                "user_id": user.id, 
                "email": user.email
            })
        else:
            print("--- LOGIN FAILED ---\n")
            error_msg = "OTP Mismatch" if not is_match else "OTP Expired"
            return Response({"error": f"Invalid Code: {error_msg}"}, status=400)
            
    except User.DoesNotExist:
        print("ERROR: User not found in DB")
        return Response({"error": "User not found"}, status=404)