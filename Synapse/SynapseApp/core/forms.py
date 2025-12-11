from django import forms
from .models import Appointment
from .models import LabAppointment
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