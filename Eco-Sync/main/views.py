from django.shortcuts import render 

def home(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')
