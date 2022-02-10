from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ClassModel, User


class StudentSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['id', 'name']

        
class ShowClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = ['name', 'teacher', 'student', 'created_at']
        
    name = serializers.CharField()
    teacher = serializers.CharField()
    student = StudentSerializer(read_only=True, many=True)
    created_at = serializers.DateTimeField()


class UpdateClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'


   
