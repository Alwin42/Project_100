from rest_framework import serializers
from django.contrib.auth.models import User
from .models import StudentProfile

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