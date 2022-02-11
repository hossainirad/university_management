from django.contrib import admin
from django.urls import include, path

from .views import ( 
    ShowClassesAPIView, 
    ShowTeacherClassesAPIView, 
    UpdateClassNameAPIView, 
    ShowStudentClassesAPIView, 
    DeleteLessonByStudentAPIView, 
    ShowUsersAPIView
    )

urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
    path('updateClass/<pk>/', UpdateClassNameAPIView.as_view()),
    path('deleteLesson/<pk>/', DeleteLessonByStudentAPIView.as_view()),     
    path('teacherClasses/<pk>/', ShowTeacherClassesAPIView.as_view()),     
    path('studentClasses/<pk>/', ShowStudentClassesAPIView.as_view()),
    path('users/', ShowUsersAPIView.as_view()),
]
