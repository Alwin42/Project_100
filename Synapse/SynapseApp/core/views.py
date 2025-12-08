from django.shortcuts import render, get_object_or_404
from .models import Doctor, Hospital
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
    # Fetch all hospital records from the database
    hospitals = Hospital.objects.all()
    
    context = {
        'hospitals': hospitals
    }
    
    # Render the HTML template with the data
    return render(request, 'hospitals.html', context)

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

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
        # We use email as the username for simplicity
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # 5. Create Profile
        # Handle empty numeric fields to avoid errors
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
    # select_related optimizes the query to fetch Hospital details in one go
    doctors = Doctor.objects.select_related('hospital').all()
    
    context = {
        'doctors': doctors
    }
    return render(request, 'appointment.html', context)

# 2. View to handle the actual booking form submission
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
            return redirect('dashboard') # Redirect to dashboard or success page
    else:
        form = AppointmentForm()

    context = {
        'doctor': doctor,
        'form': form
    }
    # You will need a simple 'booking_form.html' for this view, 
    # but for now, we focus on the appointment.html requested.
    return render(request, 'booking_form.html', context)