from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import ClassModel, LessonModel

User = get_user_model()

class ClassChangeForm(forms.ModelForm):

    class Meta:
        model = ClassModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         list_teacher = User.objects.filter(access=3)
         self.fields['teacher'].queryset = list_teacher
         list_student = User.objects.filter(access=2)
         self.fields['student'].queryset = list_student


admin.site.register(User)
admin.site.register(LessonModel)


class ClassModelAdmin(admin.ModelAdmin):
    form = ClassChangeForm
    list_display    = [
        'name',
        'teacher',
    ]

admin.site.register(ClassModel, ClassModelAdmin)