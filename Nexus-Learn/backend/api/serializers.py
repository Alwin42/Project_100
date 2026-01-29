from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    StudentProfile, 
    Task, 
    Reminder, 
    Timetable, 
    Notification, 
    Subject, 
    PersonalFile
)

# --- YOUR EXISTING AUTH SERIALIZERS ---

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['age', 'dob', 'college', 'course']

class UserSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        # Create the User
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            email=validated_data.get('email', '')
        )
        # Create the linked Student Profile
        StudentProfile.objects.create(user=user, **profile_data)
        return user


# --- NEW DASHBOARD SERIALIZERS (ADD THESE) ---

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
    # This read-only field lets us see the Subject Name (e.g. "Math") instead of just ID "1"
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