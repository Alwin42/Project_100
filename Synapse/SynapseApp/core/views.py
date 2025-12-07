from django.shortcuts import render, get_object_or_404
from .models import Doctor, Hospital

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

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request,'register.html')

