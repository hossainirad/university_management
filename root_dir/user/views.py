from django.contrib.auth import get_user_model
from rest_framework import permissions, serializers
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.response import Response

from .models import ClassModel
from .permissions import IsStaff, IsTeacher
from .serializers import (CreateClassSerializer, CreateUserSerializer,
                          ShowClassesSerializer, ShowStudentClassSerializer,
                          ShowUserSerializer, UpdateClassesSerializer)

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
    serializer_class = ShowStudentClassSerializer

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

        return Response("The lesson deleted.")


class DeleteStudentAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
    serializer_class = ShowClassesSerializer

    def get(self, request, *args, **kwargs):
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        try:
            student = User.objects.get(id= int(self.kwargs['id']))
        except Exception:
            raise serializers.ValidationError({
                "error_ms": "This ID doesn't exist."
            })
        if request.user.id == student_class.teacher.id:
            student.lesson_list.remove(student_class)
            return Response("The student deleted.")
        else:
            return Response("You can't delete students from this class.")


class CreateUserAPIView(CreateAPIView):
    permission_classes = [IsStaff, ]
    
    queryset = ClassModel.objects.all()
    serializer_class = CreateUserSerializer


class CreateClassAPIView(CreateAPIView):
    permission_classes = [IsStaff , IsTeacher]
    
    queryset = ClassModel.objects.all()
    serializer_class = CreateClassSerializer
    










