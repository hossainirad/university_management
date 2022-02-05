## for creating custom user table
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
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
    is_active = models.BooleanField(default=True, verbose_name='فعال؟') 
    is_admin = models.BooleanField(default=False, verbose_name='کارمند؟') 
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name='نام')
    mobile = PhoneNumberField(unique=True, verbose_name='شماره همراه')
    access = models.PositiveSmallIntegerField()

    USERNAME_FIELD = 'mobile'
    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return str(self.mobile)