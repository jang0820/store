from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250)
    postal = models.CharField(max_length=20)
    money = models.IntegerField(default=0)
