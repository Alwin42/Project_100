from django.db import models

class Car(models.Model):
    # --- CORRECT CHOICES FORMAT ---
    CATEGORY_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Coupe', 'Coupe'),
        ('Luxury', 'Luxury'),
    ]
    
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),      # <--- Must be ('Value', 'Label')
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('CNG+Petrol', 'CNG + Petrol'),
    ]
    
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]
    # ------------------------------

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