from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Car(models.Model):
    CATEGORY_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Luxury', 'Luxury'),
    ]
    
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),      
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('CNG+Petrol', 'CNG + Petrol'),
    ]
    
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    # Basic Info
    manufacturer = models.CharField(max_length=100, default="Unknown")
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50, default="White")
    tag = models.CharField(max_length=50, default="Best")
    
    # Technical Details
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Sedan')
    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES, default='Petrol')
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, default='Manual')
    mileage = models.FloatField(help_text="Mileage in km/L", default=15.0)
    
    # Owner & Location Info
    owner_name = models.CharField(max_length=100, default="Admin")
    owner_phone = models.CharField(max_length=20, default="0000000000")
    location = models.TextField(help_text="Pickup Address", default="Kochi, Kerala")
    
    # Rental Info
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)
    
    # ID Proof
    id_proof = models.ImageField(upload_to='id_proofs/', blank=True, null=True)
    is_verified = models.BooleanField(default=False) 

    def is_otp_valid(self):
        if not self.otp_created_at: return False
        now = timezone.now()
        return now - self.otp_created_at < datetime.timedelta(minutes=5)

    def __str__(self):
        return f"{self.user.email} - {'Verified' if self.is_verified else 'Pending'}"

# --- NEW MODEL: TRACKS RENTALS ---
class Rental(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),      # User clicked book, awaiting payment/approval
        ('Confirmed', 'Confirmed'),  # Payment done, booking confirmed
        ('Active', 'Active'),        # User has picked up the car
        ('Completed', 'Completed'),  # Car returned
        ('Cancelled', 'Cancelled'),
    ]

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rentals')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rentals')
    
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} rented {self.car.model} ({self.status})"

class PaymentSettings(models.Model):
    upi_id = models.CharField(max_length=50, help_text="e.g., yourname@oksbi")
    qr_image = models.ImageField(upload_to='payment_qr/')
    
    class Meta:
        verbose_name = "Payment QR Code"
        verbose_name_plural = "Payment Settings"

    def __str__(self):
        return f"UPI Settings ({self.upi_id})"