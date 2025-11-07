# main/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# --- User Profile Model ---
# This model extends the built-in User model to add an address and full name.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# --- Signals to auto-create/update UserProfile ---
# These functions automatically create a UserProfile when a new User is created.

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# --- Waste Type Model ---
# This model stores the different types of waste (e.g., "Organic", "Plastic").

class WasteType(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="e.g., Organic, Plastic, E-Waste")

    def __str__(self):
        return self.name


# --- Collection Request Model ---
# This model stores a user's request for a waste pickup.

class CollectionRequest(models.Model):
    # Status choices for the request
    STATUS_PENDING = 'Pending'
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_COMPLETED = 'Completed'
    STATUS_CANCELLED = 'Cancelled'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    # --- Relationships ---
    # Link to the user who made the request
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection_requests')
    
    # Link to the type of waste being collected
    # If a WasteType is deleted, set this field to NULL, not delete the whole request
    waste_type = models.ForeignKey(WasteType, on_delete=models.SET_NULL, null=True)

    # --- Request Details ---
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    address = models.TextField(help_text="The full address for this specific pickup.")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)
    requested_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Request from {self.user.username} for {self.waste_type.name} on {self.preferred_date}"


# --- Illegal Dumping Report Model ---
# This model stores reports of illegal dumping incidents.

class IllegalDumpingReport(models.Model):
    location = models.CharField(max_length=255, help_text="e.g., Near Marine Drive")
    description = models.TextField()
    
    # 'upload_to' specifies a subdirectory within your media root
    image = models.ImageField(upload_to='dumping_reports/', blank=True, null=True)
    
    reported_at = models.DateTimeField(default=timezone.now)
    
    # Optional link to the user who reported it (if they were logged in)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Report at {self.location} on {self.reported_at.date()}"
    
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )
    
    # The request this review is for
    request = models.OneToOneField(CollectionRequest, on_delete=models.CASCADE, related_name='review')
    # The user who wrote the review
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.request.id} by {self.user.username}"