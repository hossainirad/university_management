from django.contrib import admin
from django.urls import path,include
from .views import ShowClassesAPIView


urlpatterns = [
    path('classes/', ShowClassesAPIView.as_view()),
]
