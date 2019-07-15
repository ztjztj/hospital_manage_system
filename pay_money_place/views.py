from django.shortcuts import render

def index(request):
    return render(request,'pay_money_place/index.html')

def enter_index(request):
    return render(request,'pay_money_place/enter_index.html')

def outer_index(request):
    return render(request,'pay_money_place/outer_index.html')

def give_medicine_index(request):
    return render(request,'pay_money_place/give_medicine_index.html')

def pay_money_place_password(request):
    return render(request,'pay_money_place/pay_money_place_password.html')

def enter_add(request):
    return render(request,'pay_money_place/enter_add.html')

def outer_detail(request):
    return render(request,'pay_money_place/outer_detail.html')

def give_detail(request):
    return render(request,'pay_money_place/give_detail.html')

def medicine_look(request):
    return render(request,'pay_money_place/medicine-look.html')