from operator import mod
from turtle import title
from django.db import models
from django.utils.timezone import now

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=70)

    def __str__(self):
        return str(self.id)


class Teacher(models.Model):
    Teacher_Name = models.CharField(max_length=30, null=True)
    Teacher_Email = models.EmailField(max_length=60, null=True)
    Female = 'F'
    Male = 'M'
    Others = 'O'
    Gender = [
        (Female,'female'),
        (Male, 'male' ),
        (Others, 'Others' ),
    ]
    Teacher_Gender = models.CharField(max_length=30, choices=Gender, default=Female)

    def __str__(self):
        return str(self.Teacher_Name)
        
class Post(models.Model):
    CATEGORY = (
        ('TEACHER', 'teacher'),
        ('STUDENT', 'student'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    slug = models.CharField(max_length=100, default=title) 
    email = models.EmailField()
    salary = models.IntegerField()
    details = models.TextField()
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    detail_time = models.DateTimeField(default=now)     

