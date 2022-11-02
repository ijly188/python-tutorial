from django.contrib import admin
from blog.models import UserProfile as UserModel
from blog.models import Article as ArticleModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(ArticleModel)