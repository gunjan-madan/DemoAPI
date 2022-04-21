from django.db import models

# Create your models here.
class Student(models.Model):
    studentID= models.IntegerField(primary_key=True)
    studentName= models.CharField(max_length=60)
    studentClass= models.CharField(max_length=20)