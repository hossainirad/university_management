from django.contrib.auth import get_user_model
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from .models import ClassModel, User


class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']


class ShowClassesSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    teacher = serializers.CharField()
    student = ShowUserSerializer(read_only=True, many=True)

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'teacher', 'student', 'created_at']


class UpdateClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'


class ShowStudentClassSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    teacher = serializers.CharField()
    missed_deadline = serializers.SerializerMethodField()

    class Meta:
        model = ClassModel
        fields = ['id', 'name', 'teacher', 'missed_deadline']

    def get_missed_deadline(self, obj):
        check_permission = obj.has_missed_deadline()
        return check_permission


class CreateUserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['name', 'mobile', 'access']        


class CreateClassSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ClassModel
        fields = ['name', 'teacher']
    
    
class LoginSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField()
    password = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['phone_number', 'password']
        
