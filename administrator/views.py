from django.shortcuts import render

def administrator_index(request):
    return render(request, 'administrator/index.html')

def doctor_manage(request):
    return render(request,'administrator/doctor_manage.html')

def user_manage(request):
    return render(request,'administrator/user_manage.html')

def administrator_password(request):
    return render(request,'administrator/administrator_password.html')

def user_manage_add(request):
    return render(request,'administrator/user_manage_add.html')

def doctor_manage_edit(request):
    return render(request,'administrator/doctor_manage_edit.html')

def doctor_manage_look(request):
    return render(request,'administrator/doctor_manage_look.html')

def doctor_manage_add(request):
    return render(request,'administrator/doctor_manage_add.html')