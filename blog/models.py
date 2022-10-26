from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    account     = models.CharField(max_length=150)
    email       = models.EmailField(max_length=150)
    first_name  = models.EmailField(max_length=150)
    last_name   = models.EmailField(max_length=150)
    phone       = models.CharField(max_length=150)
    password    = models.CharField(max_length=150)
    createtime  = models.DateTimeField(auto_now_add=True,auto_now=False)
    updatetime  = models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self) :
        return self.account

    # validator 好像可以在這邊加