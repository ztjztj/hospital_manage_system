from django.contrib import admin
from django.urls import path,include
from login_register import views

urlpatterns = [
    path('login/', views.Login,name="login"),
    path('',views.Register.as_view(),name='register'),
    path('information/<int:id>',views.information_1,name='information_1'),
    path('card_own/',views.Card_own.as_view(),name='card_own'),
    path('generate_code/',views.generate_code,name='vcode'),
    path("profession/",views.profession,name="profession"),
    path('get_phone_code/',views.get_phone_code,name="get_phone_code"),

]