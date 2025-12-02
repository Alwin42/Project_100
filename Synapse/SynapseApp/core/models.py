from django.db import models
from django.contrib.auth.models import User

# 1. Profile Model: Extended for Health Status & Personal Info
class Profile(models.Model):
    # Choices for standardization
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    # Link to the default User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # Contact Details
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # Physical Stats
    age = models.PositiveIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Weight in KG")
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Height in CM")
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    
    # Medical History
    disease_1 = models.CharField(max_length=100, blank=True, null=True, help_text="Primary existing condition")
    disease_2 = models.CharField(max_length=100, blank=True, null=True, help_text="Secondary existing condition")
    allergies = models.TextField(blank=True, null=True, help_text="Any known allergies")

    def __str__(self):
        return f"Profile of {self.user.username}"

# 2. Hospital Model
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hospitals/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    
    # Ratings & Fees
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0) # e.g., 4.5
    minimum_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 3. Laboratory Model
class Laboratory(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='labs/', blank=True, null=True)
    description = models.TextField(blank=True)
    is_verified = models.BooleanField(default=False)
    
    # Lab specifics
    start_time = models.TimeField()
    close_time = models.TimeField()
    minimum_fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# 4. Doctor Model
class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.TimeField()
    available_to = models.TimeField()

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

# 5. Appointment Model
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    # Django automatically creates 'user_id' and 'doctor_id' columns
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    # Fee is frozen at booking time to prevent hikes
    booking_fee_paid = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} with {self.doctor.name}"

# 6. Message/Complaint Model
class Message(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('READ', 'Read'),
        ('RESOLVED', 'Resolved'),
    ]

    # Optional link to user if logged in, otherwise just stores name/email
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=400) # Max length 400
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message: {self.subject} ({self.status})"