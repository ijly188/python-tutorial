from django.urls import path
from . import views
from blog.view import article as articleView
from blog.view import user as userView

urlpatterns = [
    path('', views.index, name = "index"),

    # test router
    
    # article
    path('articles', articleView.articleList, name = "articleList"),
    # createArticle
    path('create-article', articleView.createArticle, name = "createArticle"),
    # getArticleById
    # updateArticle
    # deleteArticleById

    path('author', articleView.author, name = 'author'),

    # member
    path('register', userView.register, name = "register"),
    path('login', userView.login, name = "login"),
    path('logout', userView.logout, name = "logout"),
    path('member-info', userView.getMemberInfo, name = "getMemberInfo"),
    path('member-update', userView.updateMemberInfo, name = "updateMemberInfo"),
    path('forget-password', userView.forgetPassword, name = "forgetPassword"),
]
