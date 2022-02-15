from django.contrib import admin
from django.urls import include, path
 

from .views import ( 
    ShowClassesAPIView, 
    ShowTeacherClassesAPIView, 
    UpdateClassNameAPIView, 
    ShowStudentClassesAPIView, 
    DeleteLessonByStudentAPIView, 
    ShowUsersAPIView,
    DeleteStudentAPIView,
    CreateUserAPIView,
    CreateClassAPIView,
    LoginAPIView
    )

urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
    path('update-class/<pk>/', UpdateClassNameAPIView.as_view()),
    path('delete-lesson/<pk>/', DeleteLessonByStudentAPIView.as_view()),  
    path('delete-student/<pk>/<id>/', DeleteStudentAPIView.as_view()), # pk = class ID , id = student ID       
    path('teacher-class/', ShowTeacherClassesAPIView.as_view()),     
    path('student-class/', ShowStudentClassesAPIView.as_view()),
    path('users/', ShowUsersAPIView.as_view()),
    path('create-student/', CreateUserAPIView.as_view()),
    path('create-class/', CreateClassAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
