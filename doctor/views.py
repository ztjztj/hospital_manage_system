from django.shortcuts import render


def index(request):
    return render(request,'doctor/index.html')


def patient_list(request):
    return render(request,'doctor/patient_list.html')


def doctor_password(request):
    return render(request,'doctor/doctor_password.html')
