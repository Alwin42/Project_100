from django.contrib import admin
from .models import (
    StudentProfile, 
    Subject, 
    Timetable, 
    Task, 
    Reminder, 
    Notification, 
    PersonalFile, 
    Expense, 
    Activity, 
    Note
)

admin.site.register(StudentProfile)
admin.site.register(Subject)
admin.site.register(Timetable)
admin.site.register(Task)
admin.site.register(Reminder)
admin.site.register(Notification)
admin.site.register(PersonalFile)
admin.site.register(Expense)
admin.site.register(Activity)
admin.site.register(Note)