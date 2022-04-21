
from django.contrib import admin
from django.urls import path
from studentapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getstudent/<int:id>', views.get_studentdetail),
    path('getstudent/', views.get_students),
    path('createstudent/',views.create_student),
    path('studentapi/', view=views.student_api)
]
