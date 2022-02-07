from django.contrib.auth import get_user_model
from .models import ClassModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShowClassesSerializer

from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView

Class = ClassModel

class ShowClassesAPIView(ListAPIView):

    serializer_class = ShowClassesSerializer
    queryset = Class.objects.all()

    # def get(self, request, *args, **kwargs):
    #     users = User.objects.all()
    #     print(users)
    #     return Response('iiiiiiii')