from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClassModel, LessonModel
from .serializers import ShowClassesSerializer, UpdateClassesSerializer, StudentSerializer

User = get_user_model()

class ShowClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()


class ShowUsersAPIView(ListAPIView):
    serializer_class = StudentSerializer
    queryset = User.objects.all()
    

class ShowTeacherClassesAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
    users = User.objects.all()

    def get(self, request, *args, **kwargs):
        teacherClasses = list()
        obj = ClassModel.objects.all()
        class_obj = ClassModel.objects.filter(teacher=self.users[int(self.kwargs['pk'])])
        for i in range(0,len(class_obj)):
            s = ShowClassesSerializer(class_obj[i])
            teacherClasses.append(s.data)    
        return Response(teacherClasses)


class ShowStudentClassesAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
       
    def get(self, request, *args, **kwargs):
        studentClasses = list()
        obj = ClassModel.objects.all()
        for i in range(0,len(obj)):
            s = ShowClassesSerializer(obj[i])
            data = s.data    
            for j in range(0, len(data['student'])):
                if int(self.kwargs['pk']) == data['student'][j]['id']:
                    class_obj = ClassModel.objects.filter(name=data['id'])
                    studentClasses.append(s.data)

        return Response(studentClasses)            


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


class DeleteLessonByStudentAPIView(DestroyAPIView):
    queryset = ClassModel.objects.all()

    # def get(self, request, *args, **kwargs):
    #     userClass= list()
    #     if request.user.is_authenticated:
    #         print('this is hereeee')
    #         userID = request.user.id
    #         classes = ClassModel.objects.all()
    #         for i in range(0, len(classes)):
    #             if classes[i].id == int(self.kwargs['pk']):
    #                 s = ShowClassesSerializer(classes[i])
    #                 data = s.data 
    #                 userClass = s.data 
    #         for i in range(0, len(userClass['student'])):
    #             if userClass['student'][i]['id'] == userID:
    #                 userClass['student'][i].delete()
    #         print(userClass['student'])
            
    #     return Response("")    
    # classModel = ClassModel()
    # def get(self, request, *args, **kwargs):
    #     teacher = self.get_object()

    #     if self.classModel.has_missed_deadline(self) :
    #         teacher.delete()
    #         return Response('Class deleted.', )
    #     return Response('You miss a deadline.',)


