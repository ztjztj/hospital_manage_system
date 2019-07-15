from django.contrib import admin
from django.urls import path,include
from pay_money_place import views

urlpatterns = [
    path("",views.index,name="index"),
    path("enter_index/",views.enter_index,name="enter_index"),
    path("outer_index/",views.outer_index,name="outer_index"),
    path("give_medicine_index/",views.give_medicine_index,name="give_medicine_index"),
    path("password/",views.pay_money_place_password,name="pay_money_place_password"),
    path("enter_add/",views.enter_add,name="enter_add"),
    path("outer_detail/",views.outer_detail,name="outer_detail"),
    path("give_detail/",views.give_detail,name="give_detail"),
    path("medicine_look/",views.medicine_look,name="medicine_look")
]