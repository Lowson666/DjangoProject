# -*- coding: utf-8 -*-
from django.db import models


class UserInfo(models.Model):
    #用户名
    uname = models.CharField(max_length=20)
    # 密码
    upwd = models.CharField(max_length=40)
    #邮箱
    uemail = models.CharField(max_length=30)
    #地址
    uaddress = models.CharField(max_length=100)
    #收货地址
    uadses = models.CharField(max_length=20)
    #邮编
    upostcode = models.CharField(max_length=6)
    #电话
    uphone = models.CharField(max_length=11)