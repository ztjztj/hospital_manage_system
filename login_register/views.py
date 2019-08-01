from django.shortcuts import render,redirect,HttpResponse,reverse
from django import views,forms
from login_register.forms import *
import time,random
from django.http import JsonResponse



def Login(request):
   if request.method == "GET":
        return render(request,'login_register/login.html',{'wzp':id})
   else:
        # 获取用户输入的验证码
        vcode_input = request.POST.get('vcode')
        # 获取session中存储的验证码
        vcode_session = request.session.get('verifycode')
        # 进行验证码的校验
        if vcode_input != vcode_session:
            # 验证码错误
            return render(request,'login_register/login.html',{'code_error':'验证码错误'})
        name = request.POST.get('user_number')
        pwd = request.POST.get('user_pwd')
        # status = UserInfo.objects.get('user_status')
        user_one = UserInfo.objects.filter(user_number=name)
        for i in user_one:
            if i.user_status ==  "禁用":
                return render(request,"login_register/login.html",{"cuo_wu":"该账号未启用"})
        if UserInfo.objects.filter(user_number=name,user_password=pwd).exists():
            u = UserInfo.objects.filter(user_number=name,user_password=pwd)
            for i in u:
                request.session['u_id'] = i.user_name
                request.session.set_expiry(0)
                a = request.session.get("u_id")
                return redirect(reverse("index",kwargs={"user_name":a}))
        else:
            return render(request,'login_register/login.html')
    #
#


# class Login(views.View):
#     def get(self,request):
#         return render(request,'login_register/login.html')
#     def post(self,request):
#         # 获取用户输入的验证码
#         vcode_input = request.POST.get('vcode')
#         # 获取session中存储的验证码
#         vcode_session = request.session.get('verifycode')
#         # 进行验证码的校验
#         if vcode_input != vcode_session:
#             # 验证码错误
#             return render(request,'login_register/login.html',{'code_error':'验证码错误'})
#         number = request.POST.get('user_number')
#         pwd = request.POST.get('user_pwd')
#         status = UserInfo.objects.get('user_status')
#         if UserInfo.objects.filter(user_number=number,user_password=pwd).exists():
#             u = UserInfo.objects.filter(user_number=number,user_password=pwd)
#             if status == '启用':
#                 return
#
#                 for i in u:
#                     request.session['u_id'] = i.id
#                     request.session.set_expiry(0)
#             return redirect("index")
#         else:
#             return render(request,'login_register/login.html',{'errmsg':'用户名或密码错误'})



class Register(views.View):
    def get(self,request):
        depart = Department.objects.all()
        role = Role.objects.all()
        print(depart,role)
        return render(request,'login_register/register.html',{"depart":depart,"role":role})
    def post(self,request):
        phone_code_sys = request.session['phone_code']  # 系统生成的验证码
        verify_code_input = request.POST.get('verify_code')
        if verify_code_input != phone_code_sys:
            return render(request, 'login_register/register.html', {'code_error': '验证码错误'})
        f = UserForm(request.POST)
        if f.is_valid():
            number = request.POST.get('user_number')
            password = request.POST.get('user_password')
            card = request.POST.get('user_card')
            phone = request.POST.get('user_phone')
            role_id = request.POST.get('user_role')
            depart = request.POST.get('doctor_belong')
            print(depart)
            if depart == None:
                depart=''
            F = UserInfo.objects.create(user_number=number,user_password=password,user_card=card,user_phone=phone,user_role_id=int(role_id),doctor_belong_id=int(depart))
            F.save()
            wzp = UserInfo.objects.get(user_number=number)
            return render(request, 'login_register/complete_information.html', {'wzp':wzp})
        else:

            print(f.errors.get_json_data())
            depart = Department.objects.all()
            role = Role.objects.all()
            return render(request, 'login_register/register.html', {"depart": depart, "role": role})


def information_1(request,id):
    print(id)
    print("*******************")
    if request.method == "GET":

        return render(request, 'login_register/complete_information.html', {'wzp':id})
    else:
        print("111111111111111111111111111111")

        u = UsertwoForm(request.POST)
        if u.is_valid():
            print("111111111111111111111111111111")
            name = request.POST.get('user_name')
            age  = request.POST.get('user_age')
            gender = request.POST.get('user_gender')
            level = request.POST.get('user_level')
            email = request.POST.get('user_email')
            b = UserInfo.objects.get(pk=id)
            b.user_name = name
            b.user_age = age
            b.user_gender = gender
            b.user_level = level
            b.user_email = email
            b.save()
            return redirect("login")
        else:
            print(u.errors.get_json_data())
            return render(request, 'login_register/complete_information.html')


class Card_own(views.View):
    def get(self,request):
        return render(request,"login_register/register.html")
    def post(self,request):
        u = UserForm(request.POST)
        id = request.POST.get("id")
        id_1 = "0123456789X"
        id_2 = "0123"
        id_3 = "01"
        time_now = time.strftime('%Y', time.localtime(time.time()))
        for i in id:
            if i in id_1:
                pass
            else:
                return redirect("register")
        if id[0] == '1' and id[17] in id_1 and id[10] in id_3 and id[12] in id_2:
            pass
        else:
            return redirect("register")
        a = int(time_now) - int(id[6:10])
        if 18 <= a <= 60:
            pass
        else:
            return redirect("register")

        if u.is_valid():
            u.save()
            return redirect("information")
        else:
            return redirect("register")

# 图片验证码
from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO
def generate_code(request):
    """
    生成验证码
    :param request:
    :return:
    """
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100 # 验证码图片的宽度
    height = 25 # 验证码图片的高度
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor) # 实例化图片对象并指定宽高和背景颜色
    # 创建画笔对象
    draw = ImageDraw.Draw(im) # 基于im对象得到画笔对象
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        # (2,5)
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill) # 使用画笔画噪点并指定噪点的颜色

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    # 得到四位验证码
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('verify_app/FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

# 手机验证码
from login_register.phone_sys.phone_sys import *
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt # 使用ajax发送post请求时必须使用的装饰器
def get_phone_code(request):
    """
    获取手机验证码
    :param request:
    :return:
    """
    phone = request.POST.get('phone') # 得到手机号码
    # 1.得到生成的验证码
    phone_code = get_code(alpha=False)
    print('phone_code_sys='+str(phone_code))
    request.session['phone_code'] = phone_code
    # 2.向指定手机号码发送验证码
    result = send_sms(phone,phone_code)
    print(type(result)) # str
    print(result)
    return HttpResponse(result)

# 定义装饰器
def login_required(view_func):
    #定义闭包函数
    def wrapper(request,*args,**kwargs):
        if not request.session.has_kry(''):
            return redirect('login')
        return view_func(request,*args,**kwargs)
    return wrapper

# 职业
def profession(request):
    role_id = request.POST.getlist('select')[0]

    if role_id == '1':

        return JsonResponse({'status':1})
    elif role_id == '2':
        return JsonResponse({'status':2})
    elif role_id == '3':
        return JsonResponse({'status':3})
    elif role_id == '4':
        return JsonResponse({'status':4})
    else:
        return JsonResponse({'status':0})

