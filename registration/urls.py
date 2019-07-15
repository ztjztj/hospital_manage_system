from django.contrib import admin
from django.urls import path,include
from registration import views

urlpatterns = [
    path("",views.index,name="index"),
    path("registration_index/",views.registration_index,name="registration_index"),
    path("registration_add/",views.registration_add,name="registration_add"),
    path("registration_edit/",views.registration_edit,name="registration_edit"),
    path("registration_look/",views.registration_look,name="registration_look"),
    path("registration_password/",views.registration_password,name="registration_password")
]