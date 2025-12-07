from django.shortcuts import render
from .models import Doctor , Hospital
def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
   
    all_doctors = Doctor.objects.select_related('hospital').all()
    
    context = {
        'doctors': all_doctors
    }
    return render(request, 'doctor.html', context)

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request,'register.html')

def hospital_list(request):
    """
    View to display all hospitals.
    Fetches all hospital records from the database and passes them to the template.
    """
    # You might want to add .order_by('-rating') or similar
    hospitals = Hospital.objects.all()
    
    context = {
        'hospitals': hospitals
    }
    
    return render(request, 'hospitals.html', context)