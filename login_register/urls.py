from django.contrib import admin
from django.urls import path,include
from login_register import views

urlpatterns = [
    path('', views.login,name="login"),
]