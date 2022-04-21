from rest_framework import serializers
from .models import Student
class StudentSerializers(serializers.Serializer):
    studentID= serializers.IntegerField()
    studentName= serializers.CharField(max_length=60)
    studentClass= serializers.CharField(max_length=20)

    def create(self, data):
        return Student.objects.create(**data)   