from django.utils import timezone

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not mobile:
            raise ValueError('Users must have a mobile')
        user = self.model(mobile=mobile, *extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def validate_password(self, value: str):
       return make_password(value)
        

    def create_superuser(self, mobile, password=None):
        """Creates and saves a new super user"""
        user = self.create_user(mobile, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user




class User(AbstractBaseUser, PermissionsMixin):
    """
    access roles:
    1 ==> staff
    2 ==> student
    3 ==> teacher
    4 ==> superuser
    """

    is_active = models.BooleanField(default=True, verbose_name='فعال؟') 
    is_admin = models.BooleanField(default=False, verbose_name='کارمند؟') 
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='نام')
    mobile = PhoneNumberField(unique=True, verbose_name='شماره همراه')
    access = models.PositiveSmallIntegerField(default=1)

    USERNAME_FIELD = 'mobile'
    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return str(self.mobile)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class LessonModel(models.Model):
    name = models.CharField(max_length=20, verbose_name='عنوان')
    credit = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=6, null=True, blank=True,verbose_name='سریال')

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'
        db_table = 'user_lesson'

    def __str__(self):
        return self.name


class ClassModel(models.Model):

    name = models.OneToOneField(LessonModel, on_delete=models.CASCADE, primary_key=True, verbose_name='کلاسهای دروس')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_list', verbose_name='استاد')
    student = models.ManyToManyField(User, related_name='lesson_list', verbose_name='دانشجو')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'
        db_table = 'user_class'

    def __str__(self):
        return str(self.name)
    
    def get_created_at(self):
        return self.created_at

    def has_missed_deadline(self):
        current_datetime = timezone.now()
        if self.created_at + relativedelta(days=14) > current_datetime :
            return True
        return False
    
    








