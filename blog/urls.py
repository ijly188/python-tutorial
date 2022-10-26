from django.urls import path
from . import views
from blog.view import article as articleController
from blog.view import user as userController

urlpatterns = [
    path('', views.index, name = "index"),

    # test router
    
    # article
    path('articles', articleController.articleList, name = "articleList"),
    # createArticle
    # getArticleById
    # updateArticle
    # deleteArticleById
    path('author', articleController.author, name = 'author'),

    # member
    path('register', userController.register, name = "register"),
    path('login', userController.login, name = "login"),
    path('logout', userController.logout, name = "logout"),
    path('member-info', userController.getMemberInfo, name = "getMemberInfo"),
    path('member-update', userController.updateMemberInfo, name = "updateMemberInfo"),
    path('forget-password', userController.forgetPassword, name = "forgetPassword"),
]
