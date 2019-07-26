from django.db import models

class UserInfo(models.Model):  # 用户表
    user_number = models.CharField(max_length=11)
    user_password = models.CharField(max_length=10)  # 用户密码
    user_name = models.CharField(max_length=20)  # 用户名
    user_email = models.EmailField()  # 用户邮箱
    user_card = models.CharField(max_length=18)  # 用户身份证号
    user_age = models.CharField(max_length=3)  # 用户年龄
    user_gender = models.CharField(max_length=2)  # 用户性别
    user_level = models.CharField(max_length=10)  # 用户学历
    user_phone = models.IntegerField()  # 用户电话号码
    user_role = models.ForeignKey('Role', on_delete=models.CASCADE)  # 用户角色
    doctor_belong = models.ForeignKey('Department', on_delete=models.CASCADE)  # Department科室表的外键


class Role(models.Model):
    role_name=models.CharField(max_length=50)


class Department(models.Model):  # 科室
    depart_name = models.CharField(max_length=10)  # 外科


class Doctor(models.Model):  # 医生
    doctor_status = models.CharField(max_length=20, default='空闲中')  # 医生状态（是否挂号，空闲）
    waiting_number = models.IntegerField(default=0)  # 等的人数
    fk_doctor_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)  # 用户表的外键


class PatientOne(models.Model):  # 病人表(第1次住院)
    patient_name = models.CharField(max_length=6)    # 病人姓名
    patient_age=models.IntegerField()    # 病人年龄
    patient_sex=models.CharField(max_length=50)      # 病人性别
    patient_phone=models.CharField(max_length=11)      # 病人电话
    patient_card = models.CharField(max_length=18)  # 病人的身份证号
    patient_status = models.CharField(max_length=200)  # 病人的症状
    patient_history = models.CharField(default=None, max_length=600)  # 病人的过敏史
    patient_registed_time=models.DateTimeField(auto_now=True)  # 病人的挂号时间
    # patient_main_doctor = models.CharField(max_length=10)  # 病人的主治医生
    patient_is_live = models.CharField(default=None,max_length=200,null=True)  # 病人是否住院
    patient_live_day = models.CharField(default=None,max_length=300,null=True)  # 病人住院的天数
    patient_condition = models.CharField(default=None,max_length=600,null=True)  # 病人的病情
    patient_message = models.CharField(default=None,max_length=600,null=True)  # 病人的备注
    patient_one_enter_time = models.DateTimeField(auto_now_add=True,null=True)  # 病人住院的时间
    patient_one_outer_time = models.DateTimeField(auto_now_add=True,null=True)  # 病人出院的时间
    patient_over_look_doctor = models.CharField(default=0, max_length=20,null=True)  # 是否已开药
    patient_take_medicine_time = models.DateTimeField(auto_now_add=True,null=True) # 病人领药的时间
    fk_patient_doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE,null=True)  # 关联医生表
    fk_patient_depart = models.ForeignKey('Department',on_delete=models.CASCADE,null=True)  # 关联科室表

