from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClassModel
from .serializers import ShowClassesSerializer, UpdateClassesSerializer

User = get_user_model 

class ShowClassesAPIView(ListAPIView):

    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()


class UpdateClassNameAPIView(UpdateAPIView):

    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


class DeleteClassAPIView(DestroyAPIView):
    queryset = ClassModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        class_obj = ClassModel.objects.get(name=obj)
        if ClassModel.has_missed_deadline(self) :
            class_obj.delete()
            return Response('Class deleted.', )
        return Response('You miss a deadline.',)


class DeleteStudent():
    pass
