from django import forms
from django.contrib.auth.models import User  # <--- This was missing
from .models import Appointment, LabAppointment, Profile

# 1. Appointment Booking Form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'date', 'time_slot', 'reason']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded'}),
            'time_slot': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'full_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'reason': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
        }

# 2. Lab Booking Form
class LabBookingForm(forms.ModelForm):
    class Meta:
        model = LabAppointment
        fields = ['full_name', 'email', 'phone', 'date', 'time_slot', 'test_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border rounded'}),
            'time_slot': forms.TextInput(attrs={'type': 'time', 'class': 'w-full p-2 border rounded'}),
            'full_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'test_type': forms.TextInput(attrs={'class': 'w-full p-2 border rounded', 'placeholder': 'e.g. Blood Test, MRI'}),
        }

# 3. User Update Form (For Edit Profile)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
        }

# 4. Profile Update Form (For Edit Profile)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'emergency_contact', 'height', 'weight', 'blood_group', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'emergency_contact': forms.TextInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'height': forms.NumberInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500', 'step': '0.01'}),
            'blood_group': forms.Select(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500'}),
            'address': forms.Textarea(attrs={'class': 'w-full rounded-lg border-gray-300 p-3 shadow-sm focus:border-blue-500 focus:ring-blue-500', 'rows': 3}),
        }