from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClassModel, LessonModel
from .serializers import ShowClassesSerializer, UpdateClassesSerializer, ShowTeacherClassesSerializer

User = get_user_model 

class ShowClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()
        

class ShowTeacherClassesAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
    
    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        teacherName = obj.teacher
        class_obj = ClassModel.objects.filter(teacher=teacherName)
        print('################################')
       # print(self.kwargs['pk'])
        print('$$$$$$$$$$$$$$$$$$$$$$')
        print(type(class_obj[0].teacher))
        return Response('')


class ShowStudentClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


# class DeleteStudentAPIView(DestroyAPIView):
#     queryset = ClassModel.objects.all()
#     classModel = ClassModel()
#     def get(self, request, *args, **kwargs):
#         teacher = self.get_object()

#         if self.classModel.has_missed_deadline(self) :
#             teacher.delete()
#             return Response('Class deleted.', )
#         return Response('You miss a deadline.',)


