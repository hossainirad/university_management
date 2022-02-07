from django.contrib import admin
from django.urls import path,include
from .views import ShowClassesAPIView, UpdateClassNameAPIView


urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
    path('update_class/<pk>/', UpdateClassNameAPIView.as_view()),
]
