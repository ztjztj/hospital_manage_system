from django.shortcuts import render

def index(request):
    return render(request,'registration/index.html')

def registration_index(request):
    return render(request,'registration/registration_index.html')

def registration_add(request):
    return render(request,'registration/registration_add.html')

def registration_look(request):
    return render(request,'registration/registration_look.html')

def registration_edit(request):
    return render(request,'registration/registration_edit.html')

def registration_password(request):
    return render(request,'registration/registration_password.html')
