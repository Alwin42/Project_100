from django.contrib import admin
from .models import Car
from .models import Profile
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    
    list_display = ('manufacturer', 'model', 'year', 'category', 'price_per_day', 'is_available')
    
    
    list_filter = ('category', 'fuel_type', 'transmission', 'is_available')
    
    
    search_fields = ('manufacturer', 'model', 'owner_name')

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