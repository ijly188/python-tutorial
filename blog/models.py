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
    create_time  = models.DateTimeField(auto_now_add=True,auto_now=False)
    update_time  = models.DateTimeField(auto_now_add=False,auto_now=True)
    def __str__(self) :
        return self.account


class Article(models.Model):
    account = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.CharField(max_length=50, blank=False, null=False)
    create_time = models.DateTimeField(auto_now=True)
    last_edit_update = models.DateTimeField(auto_now=True)
