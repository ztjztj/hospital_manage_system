from django.contrib import admin
from django.urls import path,include
from medicine_house import views

urlpatterns = [
    path("",views.medicine_house_index,name="medicine_house_index"),
    path("medicine_house_index/",views.medicine_house,name="medicine_house"),
    path("medicine_detail/",views.medicine_detail,name="medicine_detail"),
    path("medicine_house_password/",views.medicine_house_password,name="medicine_house_password"),
    path("medicine_insert/",views.medicine_insert,name="medicine_insert")

]