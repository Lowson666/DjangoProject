# -*- coding: utf-8 -*-
from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uaddress = models.CharField(max_length=100)
    uadses = models.CharField(max_length=20)
    upostcode = models.CharField(max_length=6)
    uphone = models.CharField(max_length=11)