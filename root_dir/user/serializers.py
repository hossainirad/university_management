from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ClassModel


Class = ClassModel

class ShowClassesSerializer(serializers.Serializer):
    name = serializers.CharField()
    teacher = serializers.CharField()
    student = serializers.CharField()
    

class UpdateClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassModel
        fields = ['name']