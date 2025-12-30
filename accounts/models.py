from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .usermanager import *
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    otp = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def is_expired(self):
        print('create_at :', self.create_at)
        print('expire_at :', timezone.now() + datetime.timedelta(minutes=5))
        
        return self.create_at + datetime.timedelta(minutes=5) > timezone.now()
    