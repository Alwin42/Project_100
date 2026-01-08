from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price_per_day', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('make', 'model')