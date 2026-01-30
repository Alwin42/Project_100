from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from django.contrib.auth.models import User

# Import Models
from .models import (
    Task, Reminder, Timetable, Notification, Subject, PersonalFile,
    Expense, Activity, Note
)

# Import Serializers
from .serializers import (
    UserSerializer, UserDetailSerializer, 
    TaskSerializer, ReminderSerializer, TimetableSerializer, 
    NotificationSerializer, SubjectSerializer, PersonalFileSerializer,
    ExpenseSerializer, ActivitySerializer, NoteSerializer 
)

# --- AUTH VIEWS ---

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

# This view allows the Dashboard to fetch the logged-in user's details (College, Course, etc.)
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user

# --- HELPER CLASS ---

class BaseUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as 'student'
        serializer.save(student=self.request.user)

    def get_queryset(self):
        # Only show the logged-in user's data
        return self.queryset.filter(student=self.request.user)

# --- MAIN VIEWSETS ---

class TaskViewSet(BaseUserViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Custom ordering for Tasks (newest first)
        return super().get_queryset().order_by('-created_at')

class ReminderViewSet(BaseUserViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def get_queryset(self):
        # Custom ordering for Reminders (soonest first)
        return super().get_queryset().order_by('date_time')

class TimetableViewSet(BaseUserViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

    def get_queryset(self):
        # Custom ordering for Timetable
        return super().get_queryset().order_by('day', 'start_time')

class NotificationViewSet(BaseUserViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class SubjectViewSet(BaseUserViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class PersonalFileViewSet(BaseUserViewSet):
    queryset = PersonalFile.objects.all()
    serializer_class = PersonalFileSerializer

    def get_queryset(self):
        return super().get_queryset().order_by('-uploaded_at')

class ExpenseViewSet(BaseUserViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ActivityViewSet(BaseUserViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self):
        # Return notes where the Subject belongs to the logged-in Student
        return Note.objects.filter(subject__student=self.request.user).order_by('-created_at')