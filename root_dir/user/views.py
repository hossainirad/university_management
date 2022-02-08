from django.contrib.auth import get_user_model
from .models import ClassModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShowClassesSerializer, UpdateClassesSerializer

from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView


class ShowClassesAPIView(ListAPIView):

    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()

    # def get(self, request, *args, **kwargs):
    #     class_object = Class.objects.all()
    #     classes = ShowClassesSerializer(class_object, many=True)
    #     print('###############################')
    #     return Response(classes.data)


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()

    # def get_object(self):
    #     class_id = self.kwargs.get('pk')
    #     obj = Class.objects.get(name_id=class_id)
    #     return obj

    # def update(self, request, *args, **kwargs):
    #     return super().update(request, *args, **kwargs)