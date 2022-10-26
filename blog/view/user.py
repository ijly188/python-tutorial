import json
from datetime import datetime
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.sessions.models import Session

from blog.utilities.responseHandler import responseHandler, responseHandlerClass
from blog.service.user import UserService as UserService


def register(request):
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))

            # 其實這邊要寫 validator
            account = data["account"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            password = data["password"]
            phone = data["phone"]
            
            check_account = UserService.checkAccountExistByAccount(account)

            if check_account is None :
                UserService.createUser(account, first_name, last_name, email, phone, password)

                responseHandler.res = {
                    "status": "success",
                    "message": "註冊成功",
                    "data": {}
                }

                # 補登入行為
                auth_obj = auth.authenticate(username=account, password=password)
                request.session.create()
                auth.login(request, auth_obj)
            else :
                responseHandler.res = {
                    "status": "success",
                    "message": "註冊失敗，帳號已註冊",
                    "data": {}
                }
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res), status=200)

def login(request):
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))

            # 其實這邊要寫 validator
            account = data["account"]
            password = data["password"]
            
            auth_obj = auth.authenticate(username=account, password=password)

            if auth_obj is not None :
                if UserService.isLogin(request) == False:
                    auth_obj.check_password(password)
                    request.session.create()
                    auth.login(request, auth_obj)

                    responseHandler.res = {
                        "status": "success",
                        "message": "登入成功",
                        "data": {}
                    }
                else:
                    # 要補一種情境就是換帳號登入
                    responseHandler.res = {
                        "status": "success",
                        "message": "帳號已登入",
                        "data": {}
                    }
            else :
                responseHandler.res = {
                    "status": "success",
                    "message": "帳號密碼錯誤",
                    "data": {}
                }
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res), status=200)

def logout(request):
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))

            if UserService.isLogin(request) == True:
                auth.logout(request)

                responseHandler.res = {
                    "status": "success",
                    "message": "已登出",
                    "data": {}
                }
            else:

                responseHandler.res = {
                    "status": "success",
                    "message": "[無登入]登出",
                    "data": {}
                }

            
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res), status=200)

def getMemberInfo(request):
    if request.method == "GET": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))

            if UserService.isLogin(request) == True:
                memberInfo = UserService.getReturnUserInfoJson(request)

                responseHandler.res = {
                    "status": "success",
                    "message": "取得會員資訊",
                    "data": memberInfo
                }
            else:
                responseHandler.res = {
                    "status": "success",
                    "message": "未登入",
                    "data": {}
                }
            
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res))

def updateMemberInfo(request):
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))
            
            # 其實這邊要寫 validator
            account = data["account"]
            email = data["email"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            phone = data["phone"]

            if UserService.isLogin(request) == True:
                UserService.updateUserInfo(request)

                responseHandler.res = {
                    "status": "success",
                    "message": "更新會員資訊",
                    "data": {}
                }
            else:
                responseHandler.res = {
                    "status": "success",
                    "message": "未登入",
                    "data": {}
                }
            
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res))

def forgetPassword(request):
    if request.method == "POST": 
        try:
            data = json.loads(bytes.decode(request.body, "utf-8"))
            
            # 其實這邊要寫 validator
            password = data["password"]

            if UserService.isLogin(request) == True:
                check_account = UserService.checkSessionPassword(request, password)

                if check_account is None:
                    UserService.updateUserPassword(request)

                    # 可以隱藏的不回的部分
                    responseHandler.res = {
                        "status": "success",
                        "message": "密碼相同",
                        "data": {}
                    }
                else:
                    responseHandler.res = {
                        "status": "success",
                        "message": "更新會員密碼",
                        "data": {}
                    }
            else:
                responseHandler.res = {
                    "status": "success",
                    "message": "未登入",
                    "data": {}
                }
            
        except Exception as e:
            responseHandler.res = {
                "status": "fail",
                "message": "系統錯誤",
                "data": e
            }
    
    return JsonResponse(responseHandler.responseHandler(responseHandler.res))
    