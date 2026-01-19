from django.contrib import admin
from .models import Car, Profile, Rental, PaymentSettings

# --- CAR ADMIN ---
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'year', 'category', 'price_per_day', 'is_available')
    list_filter = ('category', 'fuel_type', 'transmission', 'is_available')
    search_fields = ('manufacturer', 'model', 'owner_name')

# --- PROFILE ADMIN ---
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'is_verified', 'has_id_proof', 'otp_created_at')
    list_filter = ('is_verified',)
    search_fields = ('user__email',)
    
    # Helper to show email in the list
    def user_email(self, obj):
        return obj.user.email

    # Helper to check if they uploaded an image
    def has_id_proof(self, obj):
        return bool(obj.id_proof)
    has_id_proof.boolean = True

# --- RENTAL ADMIN (Combined into one) ---
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'status', 'start_date', 'end_date', 'total_price', 'booked_at')
    list_filter = ('status', 'start_date')
    search_fields = ('user__username', 'car__model', 'user__email')

# --- PAYMENT SETTINGS ADMIN ---
@admin.register(PaymentSettings)
class PaymentSettingsAdmin(admin.ModelAdmin):
    # This ensures only 1 QR code can be added
    def has_add_permission(self, request):
        return not PaymentSettings.objects.exists()