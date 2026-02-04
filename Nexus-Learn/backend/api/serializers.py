from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    StudentProfile, Task, Reminder, Timetable, Notification,
    Subject, PersonalFile, Expense, Activity, Note
)

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['age', 'dob', 'college', 'course']

class UserSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'email', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            email=validated_data.get('email', '')
        )
        StudentProfile.objects.create(user=user, **profile_data)
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(source='studentprofile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'email', 'profile']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['student', 'created_at']

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
        read_only_fields = ['student', 'created_at']

class TimetableSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Timetable
        fields = '__all__'
        read_only_fields = ['student']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        read_only_fields = ['student', 'created_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['student']

class PersonalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalFile
        fields = ['id', 'title', 'file', 'uploaded_at']
        read_only_fields = ['student', 'uploaded_at']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['student', 'date']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['student', 'created_at']

class NoteSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['created_at']