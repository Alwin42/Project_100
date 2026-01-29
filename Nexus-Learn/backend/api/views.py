from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets, permissions
from .models import Task, Reminder, Timetable, Notification, Subject, PersonalFile
from .serializers import (
    TaskSerializer, ReminderSerializer, TimetableSerializer, 
    NotificationSerializer, SubjectSerializer, PersonalFileSerializer
)
# Registration View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show tasks belonging to the logged-in student
        return Task.objects.filter(student=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(student=self.request.user).order_by('date_time')

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class TimetableViewSet(viewsets.ModelViewSet):
    serializer_class = TimetableSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Timetable.objects.filter(student=self.request.user).order_by('day', 'start_time')

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(student=self.request.user).order_by('-created_at')

class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subject.objects.filter(student=self.request.user)

class PersonalFileViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PersonalFile.objects.filter(student=self.request.user).order_by('-uploaded_at')

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)