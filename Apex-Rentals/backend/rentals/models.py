from django.db import models

class Car(models.Model):
    # Basic Info
    make = models.CharField(max_length=50)   # e.g., Toyota
    model = models.CharField(max_length=50)  # e.g., Camry
    year = models.PositiveIntegerField()     # e.g., 2024
    
    # Rental Details
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    # Image (Uploads will go to a 'car_images' folder)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    
    # Meta data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"