from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.decorators import api_view
from django.http.response import JsonResponse

from blog.service.article import ArticleService as ArticleService
from blog.utilities.responseHandler import responseHandlerClass, httpStatusHandler


@api_view(['GET'])
def articleList(request):
    # if request.method == "GET": 
    try:
        articleList = ArticleService.ArticleList(request)

        result = responseHandlerClass.returnResult(responseHandlerClass("success", "取得文章清單", articleList, ''))
    except Exception as e:
        result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
    
    statusResult = httpStatusHandler.returnHttpStatus(result["status"])
    return JsonResponse(result, status=statusResult)

def createArticle(request):
    if request.method == "POST": 
        try:
            data = ArticleService.createArticleByAccount(request)

            if len(data) == 0:
                result = responseHandlerClass.returnResult(responseHandlerClass("success", "建立文章失敗", data, ''))
            else:
                result = responseHandlerClass.returnResult(responseHandlerClass("success", "建立文章成功", data, ''))

        except Exception as e:
            result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
        
        statusResult = httpStatusHandler.returnHttpStatus(result["status"])
        return JsonResponse(result, status=statusResult)

def author(request):
    return render(request, "author.html")
