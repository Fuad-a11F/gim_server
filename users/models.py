from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

class CustomAccountManage(BaseUserManager):
    def create_superuser(self, email, username, password, **other_field):
        other_field.setdefault('is_staff', True)
        other_field.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **other_field)

    def create_user(self, email, username, password, **other_field):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_field)
        user.set_password(password)
        user.save()
        return user


STATUS = [
    ('coach', 'coach'),
    ('student', 'student')
]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30, blank=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=20, choices=STATUS)
    phone = models.IntegerField(blank=True, null=True)
    experience = models.IntegerField(default=0, null=True, blank=True)
    time_begin_work = models.DateTimeField(null=True, blank=True)
    time_finish_work = models.DateTimeField(null=True, blank=True)
    time_visit_gim = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(blank=True)
    password = models.CharField(max_length=150)
    subscribe = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = CustomAccountManage()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'lastname']


    def __str__(self):
        return str(self.id)