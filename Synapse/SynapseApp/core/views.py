from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max
from .models import Doctor, Hospital, Profile, Appointment, Laboratory, LabAppointment
from .forms import AppointmentForm, LabBookingForm, UserUpdateForm, ProfileUpdateForm

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
    context = {'doctors': all_doctors}
    return render(request, 'doctor.html', context)

def hospital_list(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'hospitals.html', context)

def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    doctors = Doctor.objects.filter(hospital=hospital)
    context = {'hospital': hospital, 'doctors': doctors}
    return render(request, 'hospital_detail.html', context)

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
    # Ensure profile exists safely
    profile = getattr(request.user, 'profile', None)
    
    # NEW: Fetch user's bookings
    # We use 'patient' for doctor appointments and 'user' for lab appointments based on your models
    doctor_appointments = Appointment.objects.filter(patient=request.user).order_by('-date', '-created_at')
    lab_appointments = LabAppointment.objects.filter(user=request.user).order_by('-date', '-created_at')
    
    context = {
        'user': request.user,
        'profile': profile,
        'doctor_appointments': doctor_appointments,
        'lab_appointments': lab_appointments,
    }
    return render(request, 'dashboard.html', context)

@login_required
def edit_profile(request):
    # Ensure profile exists before editing
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'edit_profile.html', context)

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Profile fields
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

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Handle empty numeric fields
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
    context = {'doctors': doctors}
    return render(request, 'appointment.html', context)

def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            if request.user.is_authenticated:
                appointment.patient = request.user
            appointment.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('dashboard')
    else:
        form = AppointmentForm()

    context = {'doctor': doctor, 'form': form}
    return render(request, 'booking_form.html', context)

def fee_comparison(request):
    hospitals = Hospital.objects.order_by('minimum_fee')
    stats = Hospital.objects.aggregate(
        average_fee=Avg('minimum_fee'),
        lowest_fee=Min('minimum_fee'),
        highest_fee=Max('minimum_fee')
    )
    
    if stats['average_fee'] is not None:
        stats['average_fee'] = round(stats['average_fee'], 2)
    else:
        stats['average_fee'] = 0
        stats['lowest_fee'] = 0
        stats['highest_fee'] = 100 
    
    context = {'hospitals': hospitals, 'stats': stats}
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