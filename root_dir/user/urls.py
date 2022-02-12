from django.contrib import admin
from django.urls import include, path

from .views import ( 
    ShowClassesAPIView, 
    ShowTeacherClassesAPIView, 
    UpdateClassNameAPIView, 
    ShowStudentClassesAPIView, 
    DeleteLessonByStudentAPIView, 
    ShowUsersAPIView,
    DeleteStudentAPIView
    )

urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
    path('updateClass/<pk>/', UpdateClassNameAPIView.as_view()),
    path('deleteLesson/<pk>/', DeleteLessonByStudentAPIView.as_view()),  
    path('deletestudent/<pk>/<id>/', DeleteStudentAPIView.as_view()), # pk = class ID , id = student ID       
    path('teacherClasses/', ShowTeacherClassesAPIView.as_view()),     
    path('studentClasses/', ShowStudentClassesAPIView.as_view()),
    path('users/', ShowUsersAPIView.as_view()),
]
