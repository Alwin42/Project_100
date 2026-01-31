from django.urls import path, include
from .views import PersonalFileViewSet
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, UserDetailView, # <--- Added UserDetailView
    TimetableViewSet, TaskViewSet, ReminderViewSet, 
    SubjectViewSet, ExpenseViewSet, ActivityViewSet, 
    NoteViewSet, PersonalFileViewSet, NotificationViewSet
)

router = DefaultRouter()
router.register(r'timetable', TimetableViewSet, basename='timetable')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'reminders', ReminderViewSet, basename='reminder')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'expenses', ExpenseViewSet, basename='expense')     
router.register(r'activities', ActivityViewSet, basename='activity') 
router.register(r'notes', NoteViewSet, basename='note')              
router.register(r'files', PersonalFileViewSet, basename='file')
router.register(r'notifications', NotificationViewSet, basename='notification')
router.register(r'files', PersonalFileViewSet, basename='files')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user-detail'), 
    path('', include(router.urls)),
]