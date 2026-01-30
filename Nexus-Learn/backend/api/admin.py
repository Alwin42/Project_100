from django.contrib import admin
from .models import (
    StudentProfile, Subject, Timetable, Task, Reminder, 
    Notification, PersonalFile, Expense, Activity, Note
)

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'college', 'course', 'age')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'student')

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('subject', 'day', 'start_time', 'end_time', 'room_number')
    list_filter = ('day', 'subject') # Filter by day is very useful

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'is_done', 'student')
    list_filter = ('priority', 'is_done')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'is_completed', 'student')
    list_filter = ('is_completed', 'date_time')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_read', 'created_at') # Keep created_at here

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'activity_type', 'student')
    list_filter = ('activity_type',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'created_at')
    list_filter = ('subject',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('category', 'amount', 'date', 'student')
    list_filter = ('date', 'category')