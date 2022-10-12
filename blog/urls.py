from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('articles', views.articleList, name = "articleList"),
    path('author', views.author, name = 'author')
]
