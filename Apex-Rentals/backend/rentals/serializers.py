from rest_framework import serializers
from .models import Car, Rental, Profile

# 1. This converts a Car Database row -> JSON for the Payment Page
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # '__all__' means it sends EVERY field (including upi_id and qr_image)
        fields = '__all__' 

# 2. This converts Rental History -> JSON for the Dashboard
class RentalSerializer(serializers.ModelSerializer):
    # This 'nesting' puts the Car Details INSIDE the Rental JSON
    # so the dashboard can show the car name/image, not just an ID number.
    car = CarSerializer(read_only=True)
    
    class Meta:
        model = Rental
        fields = ['id', 'car', 'start_date', 'end_date', 'total_price', 'status', 'payment_proof', 'booked_at']