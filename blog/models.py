from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media',null=True,blank=True)
    
    def __str__(self):
        return self.user.username

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.faculty_name}'
    
class Branch(models.Model):
    faculty_name = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.branch_name}'

# class Predict(models.Model):
#     stid = models.IntegerField(max_length=15)
#     parent_state = models.CharField(max_length=100)
#     urban_school = models.CharField(max_length=100)
#     home_province = models.CharField(max_length=100)
#     urban_home = models.CharField(max_length=100)