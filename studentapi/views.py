import json
from django.http import HttpResponse
from django.shortcuts import render
import io
from studentapi import serializers
from studentapi.models import Student
from studentapi.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_studentdetail(request,id):
    st= Student.objects.get(studentID=id)
    ser= StudentSerializers(st)
    json_data= JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')

def get_students(request):
    st= Student.objects.all()
    ser= StudentSerializers(st, many=True)
    json_data= JSONRenderer().render(ser.data)
    return HttpResponse(json_data,content_type='application/json')
    
@csrf_exempt
def create_student(request):
    json_data= request.body
    stream= io.BytesIO(json_data)
    python_data=JSONParser().parse(stream)
    ser= StudentSerializers(data=python_data)
    if ser.is_valid():
        ser.save()
        response= {'message':'student created'}
        json_data= JSONRenderer().render(response)
        return HttpResponse(json_data,content_type='application/json')
    else:
            json_data= JSONRenderer().render(ser.errors)
            return HttpResponse(json_data,content_type='application/json')


@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id= python_data.get('id',None)
        
        if id is not None:
            stu= Student.objects.get(studentID=id)
            ser= StudentSerializers(stu)
            json_data= JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json')
        else:
            st= Student.objects.all()
            ser= StudentSerializers(st, many=True)
            json_data= JSONRenderer().render(ser.data)
            return HttpResponse(json_data,content_type='application/json')

    if request.method=='POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        ser= StudentSerializers(data=python_data)
        if ser.is_valid():
            ser.save()
            response= {'message':'student created'}
            json_data= JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data= JSONRenderer().render(ser.errors)
            return HttpResponse(json_data,content_type='application/json')