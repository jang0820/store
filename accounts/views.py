from django.shortcuts import render
from .models import MyUser
from django.db import transaction

def get_user_money(user):  #查詢儲值金餘額
    return MyUser.objects.get(username = user).money

def is_enough(user, x): #判斷餘額是否足夠支付訂單
    u = MyUser.objects.get(username = user)
    if u.money >= x: return True
    else: return False

def debit(user, x):  #扣儲值金
    u = MyUser.objects.get(username = user)
    with transaction.atomic():
        try:
            if u.money < x:
                raise ValueError("餘額不足")
            u.money = u.money - x
            u.save()
        except Exception as e:
            print("其他錯誤：",e)