"""hospital_manage_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('login_register.urls')),
    path("administrator/",include('administrator.urls')),
    path("medicine_house/",include('medicine_house.urls')),
    path("pay_money_place/",include('pay_money_place.urls')),
    path("registration/",include('registration.urls')),
    path("doctor/",include('doctor.urls'))

]
