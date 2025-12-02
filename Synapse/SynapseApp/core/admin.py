from django.contrib import admin
from .models import Profile, Hospital, Laboratory, Doctor, Appointment, Message

# 1. Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'blood_group', 'emergency_contact')

# 2. Hospital
@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'is_verified', 'rating')
    list_filter = ('is_verified', 'location')
    search_fields = ('name', 'location')

# 3. Laboratory
@admin.register(Laboratory)
class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'start_time', 'close_time')

# 4. Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital', 'consultation_fee')
    list_filter = ('specialization', 'hospital')

# 5. Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'date', 'time', 'status')
    list_filter = ('status', 'date')

# 6. Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'status', 'created_at')
    list_filter = ('status',)

