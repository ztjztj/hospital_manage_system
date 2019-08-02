from django.db import models


class UserInfo(models.Model):  # 用户表
    user_number = models.CharField(max_length=11)
    user_password = models.CharField(max_length=10)  # 用户密码
    user_name = models.CharField(max_length=20)  # 用户名
    user_email = models.EmailField()  # 用户邮箱
    user_role = models.CharField(max_length=10)  # 用户角色
    user_card = models.CharField(max_length=18)  # 用户身份证号
    user_age = models.CharField(max_length=3)  # 用户年龄
    user_gender = models.CharField(max_length=2)  # 用户性别
    user_level = models.CharField(max_length=10)  # 用户学历
    user_phone = models.IntegerField()  # 用户电话号码


# class Doctor(models.Model):
#  /   doctor_name = models.CharField(max_length=10)
#     doctor_card = models.CharField(max_length=18)

class Doctor(models.Model):  # 医生

    doctor_status = models.CharField(max_length=20, default='空闲中')  # 医生状态（是否挂号，空闲）
    waiting_number = models.IntegerField(default=0)  # 等的人数
    # doctor_belong = models.ForeignKey('Department', on_delete=models.CASCADE)  # Department科室表的外键
    fk_doctor_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)  # 用户表的外键


class DoctorMessage(models.Model):  # 医生详细信息表
    doctor_belong = models.CharField(max_length=10)  # 所属科室
    fk_doctor_message_user = models.ForeignKey('UserInfo', on_delete=models.CASCADE)


class PatientOne(models.Model):  # 病人表(第1次住院)
    patient_name = models.CharField(max_length=6)
    patient_card = models.CharField(max_length=18)  # 病人的身份证号
    patient_status = models.CharField(max_length=200)  # 病人的症状
    # patient_age = models.IntegerField()      # 病人年龄
    # patient_sex = models.CharField(max_length=50)    # 病人性别
    # patient_phone = models.CharField(max_length=11)   # 电话号
    patient_main_doctor = models.CharField(max_length=10)  # 病人的主治医生
    patient_medicine = models.CharField(max_length=20, default=None)  # 病人的药
    patient_is_live = models.CharField(default=None,max_length=200)  # 病人是否住院
    patient_live_day = models.CharField(default=None,max_length=300)  # 病人住院的天数
    patient_condition = models.CharField(default=None,max_length=600)  # 病人的病情
    patient_history = models.CharField(default=None,max_length=600)  # 病人的过敏史
    patient_message = models.CharField(default=None,max_length=600)  # 病人的备注
    patient_one_enter_time = models.DateTimeField(auto_now_add=True)  # 病人住院的时间
    patient_one_outer_time = models.DateTimeField(auto_now_add=True)  # 病人出院的时间
    patient_take_medicine_time = models.DateTimeField(auto_now_add=True) # 病人领药的时间
    patient_over_look_doctor = models.CharField(default=0,max_length=20)   # 是否已开药
    # fk_patient_doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # 关联医生表

# ★★等待添加
class PatientTwo(models.Model):  # 病人表(用户要续院)
    patient_two_enter_time = models.DateTimeField(auto_now_add=True)  # 病人住院的时间
    patient_two_outer_time = models.DateTimeField(auto_now_add=True)  # 病人出院的时间
    continue_live_day = models.CharField(default=None,max_length=200)  # 病人继续住院的天数


class Department(models.Model):  # 科室

    depart_outside = models.CharField(max_length=10)  # 外科
    depart_heart = models.CharField(max_length=10)  # 心血管科
    depart_rapid = models.CharField(max_length=10)  # 急诊科
    depart_bone = models.CharField(max_length=10)  # 骨科


class Medicine(models.Model):  # 药
    medicine_name = models.CharField(max_length=20)  # 名称
    medicine_number = models.IntegerField()  # 数量
    medicine_outer_price = models.FloatField()  # 售价
    medicine_enter_price = models.FloatField()  # 进价
    medicine_message = models.CharField(max_length=200)  # 详细描述
    # fk_medicine_type_department = models.ForeignKey('Department', on_delete=models.CASCADE)  # 药品类型和科室表关联



# 购买药品单

class Medicine_one(models.Model):
    medicine_one_name = models.CharField(max_length=20)  # 名称
    medicine_one_number = models.IntegerField()  # 数量
    medicine_one_outer_price = models.FloatField()  # 售价
    medicine_one_yes_no = models.CharField(default=0,max_length=20)  # 药方是否已提交
    fk_patient_medicine_one = models.ForeignKey('PatientOne', on_delete=models.CASCADE)  # 关联药方表


