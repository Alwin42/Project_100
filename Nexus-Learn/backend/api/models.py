from django.db import models
from django.contrib.auth.models import User

# 1. Student Profile [cite: 3]
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    dob = models.DateField()
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

# 2. Subjects [cite: 14]
class Subject(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard'), (4, 'Very Hard')])
    teacher_name = models.CharField(max_length=100, blank=True)
    youtube_link = models.URLField(blank=True)
    wiki_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

# 3. Tasks & Dashboard [cite: 6, 7]
class Task(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('High', 'High')])

class Reminder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()

# 4. Expense Tracker [cite: 8]
class Expense(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100) # e.g. Canteen, Library
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

# 5. Activity/Tools [cite: 9]
class Activity(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    activity_type = models.CharField(max_length=50) # Assignment, Sport, Hackathon
    description = models.TextField()
    image = models.ImageField(upload_to='activities/', blank=True, null=True)

# 6. Notes [cite: 17]
class Note(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/') # Handles PDF/PPT/Docx
    created_at = models.DateTimeField(auto_now_add=True)