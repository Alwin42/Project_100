from rest_framework import serializers
from .models import Rental, Car, PaymentSettings

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    # We nest the CarSerializer so the Dashboard sees car details (name, image)
    car = CarSerializer(read_only=True) 
    
    class Meta:
        model = Rental
        fields = ['id', 'car', 'start_date', 'end_date', 'total_price', 'status', 'booked_at']

class PaymentQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSettings
        fields = ['upi_id', 'qr_image']