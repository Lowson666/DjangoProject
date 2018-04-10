from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('user_page.UserInfo',on_delete=models.CASCADE)
    goods=models.ForeignKey('goods_page.GoodsInfo',on_delete=models.CASCADE)
    count=models.IntegerField(default=0)