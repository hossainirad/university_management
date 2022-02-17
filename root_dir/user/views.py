from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.throttling import UserRateThrottle
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import ClassModel
from .permissions import IsStaff, IsTeacher
from .serializers import (CreateClassSerializer, CreateUserSerializer,
                          LoginSerializer, ShowClassesSerializer,
                          ShowStudentClassSerializer, ShowUserSerializer,
                          UpdateClassesSerializer)

User = get_user_model()

class ShowClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()    


class ShowUsersAPIView(ListAPIView):
    serializer_class = ShowUserSerializer
    queryset = User.objects.all()


class ShowTeacherClassesAPIView(ListAPIView):
    """
    This view shows teacher's classes if the logged-in user is a teacher.
    """
    serializer_class = ShowClassesSerializer

    def get_queryset(self):
        qs = ClassModel.objects.filter(teacher=self.request.user)
        return qs

class ShowStudentClassesAPIView(ListAPIView):
    """
    This view shows student's classes if the logged-in user is a student.
    """
    serializer_class = ShowStudentClassSerializer

    def get_queryset(self):
        qs = ClassModel.objects.filter(student=self.request.user)
        return qs


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


class DeleteLessonByStudentAPIView(DestroyAPIView):
    """
    This view gets pk that refers to the class id and if the logged-in user is
     a student of this class, removes the student from class. 
    """
    queryset = ClassModel.objects.all()

    def get(self, request, *args, **kwargs):
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        student = request.user
        student.lesson_list.remove(student_class)

        return Response("The lesson deleted.")


class DeleteStudentAPIView(ListAPIView):
    """
    This view gets pk and id that refers to the class id and the student id.
    if the logged-in user is a teacher of this class, removes the student from class. 
    """
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
    """
    This view generate users. the logged-in user should be a stafff, so in permission_classes checks user's access.
    """
    permission_classes = [IsStaff, ]
    
    queryset = ClassModel.objects.all()
    serializer_class = CreateUserSerializer


class CreateClassAPIView(CreateAPIView):
    permission_classes = [IsStaff , IsTeacher]
    
    queryset = ClassModel.objects.all()
    serializer_class = CreateClassSerializer


class UserThrottle(UserRateThrottle):
    rate= '10/hour'


class LoginAPIView(CreateAPIView):
    """
    This view gives token for login service. if a user enter correct phone number 
    and password, this view returns access token and refresh token for login.
    by using UserThrottle class, user can only make 10 requests per hour to API.
    """
    permission_classes = []
    throttle_classes = [UserThrottle]
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):   
        mobile = request.data.get('mobile', None)
        password = request.data.get('password' , None)

        if mobile and User.objects.filter(mobile=mobile).exists():
                user = User.objects.get(mobile=mobile)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)

                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    })
        return Response("Invalid username/password.")



