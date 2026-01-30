from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    StudentProfile, 
    Task, 
    Reminder, 
    Timetable, 
    Notification, 
    Subject, 
    PersonalFile,
    Expense,   # <--- Added
    Activity,  # <--- Added
    Note       # <--- Added
)

# --- AUTH & USER SERIALIZERS ---

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['age', 'dob', 'college', 'course']

class UserSerializer(serializers.ModelSerializer):
    # This handles the nested profile creation during Registration
    profile = StudentProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            email=validated_data.get('email', '')
        )
        StudentProfile.objects.create(user=user, **profile_data)
        return user

# --- This is NEW: Use this to fetch User Profile Data for Dashboard ---
class UserDetailSerializer(serializers.ModelSerializer):
    # Nested serializer to read profile data (Course, College)
    profile = StudentProfileSerializer(read_only=True, source='studentprofile')

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'profile']


# --- DASHBOARD SERIALIZERS ---

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class TimetableSerializer(serializers.ModelSerializer):
    # Shows "Math" instead of just ID "1" in the JSON response
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Timetable
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class PersonalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalFile
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

# --- MISSING SERIALIZERS ADDED BELOW ---

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        extra_kwargs = {'student': {'read_only': True}}

class NoteSerializer(serializers.ModelSerializer):
    # Optional: Display subject name for easier reading in frontend
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        # Note is linked to Subject, not directly to User in your model, 
        # so we don't need to exclude 'student' here, but 'subject' is required.