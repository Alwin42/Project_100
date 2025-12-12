from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max
from .models import Laboratory, LabAppointment
from .forms import LabBookingForm
from .models import Hospital, Doctor

# Import your local models and forms
from .models import Doctor, Hospital, Profile, Appointment
from .forms import AppointmentForm

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    # select_related optimizes the query by fetching hospital data in the same call
    all_doctors = Doctor.objects.select_related('hospital').all()
    context = {
        'doctors': all_doctors
    }
    return render(request, 'doctor.html', context)

def hospital_list(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals
    }
    return render(request, 'hospitals.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    # The 'request.user' is automatically available.
    # We use getattr to safely get the profile, returning None if it doesn't exist
    profile = getattr(request.user, 'profile', None)
    
    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'dashboard.html', context)

def register(request):
    if request.method == 'POST':
        # 1. Get User Data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 2. Get Profile Data
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        emergency_contact = request.POST.get('emergency_contact')
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        disease_1 = request.POST.get('disease_1')
        disease_2 = request.POST.get('disease_2')
        allergies = request.POST.get('allergies')

        # 3. Validation
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        # 4. Create User
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # 5. Create Profile (Handle empty numeric fields)
        if not height: height = None
        if not weight: weight = None
        if not age: age = None

        Profile.objects.create(
            user=user,
            phone_number=phone_number,
            age=age,
            gender=gender,
            emergency_contact=emergency_contact,
            address=address,
            blood_group=blood_group,
            height=height,
            weight=weight,
            disease_1=disease_1,
            disease_2=disease_2,
            allergies=allergies
        )

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')

    return render(request, 'register.html')

def appointment_index(request):
    doctors = Doctor.objects.select_related('hospital').all()
    context = {
        'doctors': doctors
    }
    return render(request, 'appointment.html', context)

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            # If user is logged in, link them
            if request.user.is_authenticated:
                appointment.patient = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('dashboard') 
    else:
        form = AppointmentForm()

    context = {
        'doctor': doctor,
        'form': form
    }
    
    return render(request, 'booking_form.html', context)

def fee_comparison(request):
    # 1. Fetch all hospitals ordered by price
    hospitals = Hospital.objects.order_by('minimum_fee')
    
    # 2. Calculate statistics
    stats = Hospital.objects.aggregate(
        average_fee=Avg('minimum_fee'),
        lowest_fee=Min('minimum_fee'),
        highest_fee=Max('minimum_fee')
    )
    
    # 3. Handle data rounding and empty DB cases
    if stats['average_fee'] is not None:
        stats['average_fee'] = round(stats['average_fee'], 2)
    else:
        stats['average_fee'] = 0
        stats['lowest_fee'] = 0
        stats['highest_fee'] = 100 
    
    context = {
        'hospitals': hospitals,
        'stats': stats,
    }
    return render(request, 'fee_comparison.html', context)

def lab_list(request):
    labs = Laboratory.objects.all()
    return render(request, 'laboratory.html', {'labs': labs})

def book_lab(request, lab_id):
    lab = get_object_or_404(Laboratory, id=lab_id)
    if request.method == 'POST':
        form = LabBookingForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.laboratory = lab
            if request.user.is_authenticated:
                appointment.user = request.user
            appointment.save()
            messages.success(request, 'Lab test booked successfully!')
            return redirect('dashboard')
    else:
        form = LabBookingForm()
    
    return render(request, 'laboratory_booking.html', {'lab': lab, 'form': form})

def hospital_detail(request, hospital_id):
    # Fetch the specific hospital using the ID from the URL
    hospital = get_object_or_404(Hospital, id=hospital_id)
    
    # Fetch all doctors associated with this hospital
    # This assumes your Doctor model has a ForeignKey to Hospital named 'hospital'
    doctors = Doctor.objects.filter(hospital=hospital)
    
    context = {
        'hospital': hospital,
        'doctors': doctors
    }
    return render(request, 'hospital_detail.html', context)