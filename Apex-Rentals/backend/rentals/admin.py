from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    
    list_display = ('manufacturer', 'model', 'year', 'category', 'price_per_day', 'is_available')
    
    
    list_filter = ('category', 'fuel_type', 'transmission', 'is_available')
    
    
    search_fields = ('manufacturer', 'model', 'owner_name')