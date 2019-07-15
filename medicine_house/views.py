from django.shortcuts import render

def medicine_house_index(request):
    return render(request,'medicine_house/index.html')

def medicine_insert(request):
    return render(request,'medicine_house/medicine_insert.html')

def medicine_detail(request):
    return render(request,'medicine_house/medicine_detail.html')

def medicine_house(request):
    return render(request,'medicine_house/medicine_index.html')

def medicine_house_password(request):
    return render(request,'medicine_house/medicine_house_password.html')
