from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Profile, Rental

# --- CAR ADMIN ---
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'owner_name', 'price_per_day', 'is_available')
    # Use fieldsets to organize the payment info clearly
    fieldsets = (
        ('Basic Info', {'fields': ('manufacturer', 'model', 'year', 'color', 'tag')}),
        ('Technical', {'fields': ('category', 'fuel_type', 'transmission', 'mileage')}),
        ('Owner & Payment', {'fields': ('owner_name', 'owner_phone', 'upi_id', 'qr_image')}),
        ('Rental Details', {'fields': ('location', 'price_per_day', 'is_available', 'image')}),
    )

# --- PROFILE ADMIN ---
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'is_verified', 'has_id_proof')
    list_filter = ('is_verified',)
    def user_email(self, obj): return obj.user.email
    def has_id_proof(self, obj): return bool(obj.id_proof)
    has_id_proof.boolean = True

# --- RENTAL ADMIN ---
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'car', 'status', 'total_price', 'payment_preview', 'booked_at')
    list_filter = ('status', 'booked_at')
    search_fields = ('user__username', 'car__model')
    list_editable = ('status',) # Quick edit status from list view

    # Helper to show image thumbnail
    def payment_preview(self, obj):
        if obj.payment_proof:
            return format_html('<a href="{}" target="_blank"><img src="{}" width="50" height="50" style="border-radius:4px;"/></a>', obj.payment_proof.url, obj.payment_proof.url)
        return "No Proof"
    payment_preview.short_description = "Receipt"