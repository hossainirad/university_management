from django.contrib.auth import get_user_model
from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClassModel, LessonModel
from .serializers import ShowClassesSerializer, UpdateClassesSerializer, ShowUserSerializer

User = get_user_model()

class ShowClassesAPIView(ListAPIView):
    serializer_class = ShowClassesSerializer
    queryset = ClassModel.objects.all()


class ShowUsersAPIView(ListAPIView):
    serializer_class = ShowUserSerializer
    queryset = User.objects.all()
    

class ShowTeacherClassesAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
    users = User.objects.all()
        
    def get(self, request, *args, **kwargs):
        teacherID = request.user.id
        teacherClasses = list()
        obj = ClassModel.objects.all()
        class_obj = ClassModel.objects.filter(teacher=teacherID)
        for i in range(0,len(class_obj)):
            s = ShowClassesSerializer(class_obj[i])
            teacherClasses.append(s.data)    
        return Response(teacherClasses)


class ShowStudentClassesAPIView(ListAPIView):
    queryset = ClassModel.objects.all()
       
    def get(self, request, *args, **kwargs):
        studentID = request.user.id
        studentClasses = list()
        obj = ClassModel.objects.all()
        for i in range(0,len(obj)):
            s = ShowClassesSerializer(obj[i])
            data = s.data    
            for j in range(0, len(data['student'])):
                if studentID == data['student'][j]['id']:
                    studentClasses.append(data)

        return Response(studentClasses)            


class UpdateClassNameAPIView(UpdateAPIView):
    serializer_class = UpdateClassesSerializer
    queryset = ClassModel.objects.all()


class DeleteLessonByStudentAPIView(ListAPIView):
    queryset = ClassModel.objects.all()

    def get(self, request, *args, **kwargs):
        userID = request.user.id
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        student = User.objects.get(id= userID)
        student.lesson_list.remove(student_class)
        serializedClass = ShowClassesSerializer(student_class)

        return Response(serializedClass.data)


class DeleteStudentAPIView(ListAPIView):
    queryset = ClassModel.objects.all()

    def get(self, request, *args, **kwargs):
        teacherID = request.user.id
        student_class = ClassModel.objects.get(id=int(self.kwargs['pk']))
        try:
            student = User.objects.get(id= int(self.kwargs['id']))
        except Exception as e:
            return Response("This ID doesn't exist.")
        serializedClass = ShowClassesSerializer(student_class).data
        for i in range(0, len(serializedClass['student'])):
            print(len(serializedClass['student']))
            if student.id == serializedClass['student'][i]['id']:
                teacher = student_class.teacher.id
                if teacher == teacherID:
                    student.lesson_list.remove(student_class)
                else:
                    return Response("You can't delete students from this class.")

                serializedClass = ShowClassesSerializer(student_class)
                return Response(serializedClass.data)

        return Response("This student is not in the class.")
        
        







