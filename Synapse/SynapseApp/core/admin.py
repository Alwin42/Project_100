from django.contrib import admin
# Added LabAppointment to the imports below
from .models import Profile, Hospital, Laboratory, Doctor, Appointment, Message, LabAppointment

# Unregister models to prevent "AlreadyRegistered" errors during hot-reloads
models_to_unregister = [Profile, Hospital, Laboratory, Doctor, Appointment, Message, LabAppointment]
for model in models_to_unregister:
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass

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
    search_fields = ('name', 'specialization')

# 5. Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time_slot', 'status')
    list_filter = ('status', 'date')
    search_fields = ('doctor__name', 'full_name', 'email')

# 6. Message
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'email', 'status', 'created_at')
    list_filter = ('status',)

# 7. Lab Appointment
@admin.register(LabAppointment)
class LabAppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'laboratory', 'test_type', 'date', 'time_slot', 'status')
    list_filter = ('status', 'date', 'laboratory')
    search_fields = ('full_name', 'email', 'phone', 'test_type')
    list_editable = ('status',)