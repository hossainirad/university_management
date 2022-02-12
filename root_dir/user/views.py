from telnetlib import STATUS
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import ClassModel
from .serializers import (ShowClassesSerializer, ShowUserSerializer,
                          UpdateClassesSerializer)

User = get_user_model()

class ShowClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()


class ShowUsersAPIView(ListAPIView):
    serializer_class = ShowUserSerializer
    queryset = User.objects.all()


class ShowTeacherClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer

    def get_queryset(self):
        qs = ClassModel.objects.filter(teacher=self.request.user)
        return qs

class ShowStudentClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer

    def get_queryset(self):
        qs = ClassModel.objects.filter(student=self.request.user)
        return qs


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


class DeleteLessonByStudentAPIView(DestroyAPIView):
    queryset = ClassModel.objects.all()

    def get(self, request, *args, **kwargs):
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        student = request.user
        student.lesson_list.remove(student_class)
        serializedClass = ShowClassesSerializer(student_class)

        return Response(serializedClass.data)


class DeleteStudentAPIView(ListAPIView):
    queryset = ClassModel.objects.all()

    def get(self, request, *args, **kwargs):
        teacherID = request.user.id
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        try:
            student = User.objects.get(id= int(self.kwargs['id']))
        except Exception as e:
            return Response("This ID doesn't exist.")
            raise serializers.ValidationError({
                "error_ms": "This ID doesn't exist."
            })
        serializedClass = ShowClassesSerializer(student_class).data
        for i in range(0, len(serializedClass['student'])):
            print(len(serializedClass['student']))
            if student.id == serializedClass['student'][i]['id']:
                teacher = student_class.teacher.id
                if teacher == teacherID:
                    student.lesson_list.remove(student_class)
                else:
                    return Response("You can't delete students from this class.")

                serializedClass = ShowClassesSerializer(student_class)
                return Response(serializedClass.data)

        return Response("This student is not in the class.")
