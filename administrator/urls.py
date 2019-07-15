from django.contrib import admin
from django.urls import path,include
from administrator import views

urlpatterns = [
    path('', views.administrator_index,name="administrator_index"),
    path("doctor_manage/",views.doctor_manage,name="doctor_manage"),
    path("user_manage/",views.user_manage,name="user_manage"),
    path("password/",views.administrator_password,name="administrator_password"),
    path("user_manage_add/",views.user_manage_add,name="user_manage_add"),
    path("doctor_manage_add/",views.doctor_manage_add,name="doctor_manage_add"),
    path("doctor_manage_edit/",views.doctor_manage_edit,name="doctor_manage_edit"),
    path("doctor_manage_look/",views.doctor_manage_look,name="doctor_manage_look")
]