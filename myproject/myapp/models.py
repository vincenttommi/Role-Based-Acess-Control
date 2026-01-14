from django.db import models
from django.contrib.auth.models import AbstractUser
from  .models import User

class User(AbstractUser):
    ROLE_CHOICES = [
        ('administrator', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)



class Student(models.Model):
    student_id = models.CharField(max_length=10,unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="student_account")


    

