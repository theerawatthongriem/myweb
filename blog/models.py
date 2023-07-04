from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media',null=True,blank=True)
    
    def __str__(self):
        return self.user.username

class DataPredict(models.Model):
    student_id = models.CharField(max_length=150)