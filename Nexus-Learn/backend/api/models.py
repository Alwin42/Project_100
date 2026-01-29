from django.db import models
from django.contrib.auth.models import User

# 1. Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateField()
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

# 2. Subjects
class Subject(models.Model):
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'), 
        (3, 'Hard'), 
        (4, 'Very Hard')
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)
    teacher_name = models.CharField(max_length=100, blank=True)
    youtube_link = models.URLField(blank=True)
    wiki_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

# 3. Timetable (NEW - Required for Dashboard)
class Timetable(models.Model):
    DAYS = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) # Link to Subject
    day = models.CharField(max_length=3, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.subject.name} on {self.day}"

# 4. Tasks (Updated for Dashboard UI)
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'), 
        ('Medium', 'Medium'), # Added Medium to match common UI
        ('High', 'High')
    ]
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reminder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # Renamed from description for clarity
    date_time = models.DateTimeField() # Renamed from date to allow time precision
    is_completed = models.BooleanField(default=False)

# 5. Notifications (NEW - Required for Dashboard)
class Notification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# 6. Cloud / Personal Files (NEW - Required for "Cloud" Section)
class PersonalFile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # e.g., "Aadhar Card", "Resume"
    file = models.FileField(upload_to='my_cloud/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# 7. Expense Tracker
class Expense(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

# 8. Activity/Tools
class Activity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

# 9. Academic Notes
class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')
    created_at = models.DateTimeField(auto_now_add=True)