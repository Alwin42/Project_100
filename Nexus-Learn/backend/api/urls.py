from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet, 
    ReminderViewSet, 
    TimetableViewSet, 
    NotificationViewSet, 
    SubjectViewSet, 
    PersonalFileViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'reminders', ReminderViewSet, basename='reminder')
router.register(r'timetable', TimetableViewSet, basename='timetable')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'files', PersonalFileViewSet, basename='file')

urlpatterns = [
    # This automatically generates URLs like /api/tasks/, /api/subjects/, etc.
    path('', include(router.urls)),
]