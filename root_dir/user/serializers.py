from cgitb import lookup
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ClassModel, User



class ShowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

# class StudentSerializer(serializers.ModelSerializer):
#      class Meta:
#         model = User
#         fields = ['id', 'name']

# class ShowClassesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ClassModel
#         fields = [ 'name', 'teacher', 'student', 'created_at']


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
