from django.contrib import admin
from django.urls import path,include
from doctor import views

urlpatterns = [
    path("",views.index,name="index"),
    path("patient_list/",views.patient_list,name="patient_list"),
    path("doctor_password/",views.doctor_password,name="doctor_password"),
]