import json
from django.http.response import JsonResponse
from django.contrib import auth

from blog.utilities.responseHandler import responseHandlerClass, httpStatusHandler
from blog.validation.user import UserValidator
from blog.service.user import UserService as UserService


def register(request):
    if request.method == "POST": 
        validatorResult = UserValidator.registerValidator(request)

        if(validatorResult != None):
            result = responseHandlerClass.returnResult(responseHandlerClass("typeError", "註冊驗證錯誤", validatorResult, ''))

        else:
            try:
                check_account = UserService.checkAccountExistByAccount(request)

                if check_account is None:
                    createResult = UserService.createUser(request)

                    if( createResult != None):
                        result = responseHandlerClass.returnResult(responseHandlerClass("success", "註冊成功", {}, ''))

                        # 補登入行為
                        data = json.loads(bytes.decode(request.body, "utf-8"))
                        account = data["account"]
                        password = data["password"]

                        auth_obj = auth.authenticate(username=account, password=password)
                        request.session.create()
                        auth.login(request, auth_obj)
                else :
                    result = responseHandlerClass.returnResult(responseHandlerClass("success", "註冊失敗，帳號已註冊", {}, ''))

            except Exception as e:
                result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
        
        statusResult = httpStatusHandler.returnHttpStatus(result["status"])
        return JsonResponse(result, status=statusResult)

def login(request):
    if request.method == "POST": 
        validatorResult = UserValidator.loginValidator(request)

        if(validatorResult != None):
            result = responseHandlerClass.returnResult(responseHandlerClass("typeError", "登入驗證錯誤", validatorResult, ''))

        else:
            data = json.loads(bytes.decode(request.body, "utf-8"))

            # 其實這邊要寫 validator
            account = data["account"]
            password = data["password"]
            
            auth_obj = auth.authenticate(username=account, password=password)

            try:
                if auth_obj is not None :
                    if UserService.isLogin(request) == False:
                        auth_obj.check_password(password)
                        request.session.create()
                        auth.login(request, auth_obj)

                        result = responseHandlerClass.returnResult(responseHandlerClass("success", "登入成功", {}, ''))
                    else:
                        # 要補一種情境就是換帳號登入
                        result = responseHandlerClass.returnResult(responseHandlerClass("success", "帳號已登入", {}, ''))
                else :
                    result = responseHandlerClass.returnResult(responseHandlerClass("success", "帳號密碼錯誤", {}, ''))
            except Exception as e:
                result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))

        statusResult = httpStatusHandler.returnHttpStatus(result["status"])
        return JsonResponse(result, status=statusResult)

def logout(request):
    if request.method == "POST": 
        try:
            if UserService.isLogin(request) == True:
                auth.logout(request)
                result = responseHandlerClass.returnResult(responseHandlerClass("success", "已登出", {}, ''))

            else:
                result = responseHandlerClass.returnResult(responseHandlerClass("success", "[無登入]登出", {}, ''))

        except Exception as e:
            result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))

    statusResult = httpStatusHandler.returnHttpStatus(result["status"])
    return JsonResponse(result, status=statusResult)

def getMemberInfo(request):
    if request.method == "GET": 
        try:
            if UserService.isLogin(request) == True:
                memberInfo = UserService.getReturnUserInfoJson(request)

                result = responseHandlerClass.returnResult(responseHandlerClass("success", "取得會員資訊", memberInfo, ''))
            else:
                result = responseHandlerClass.returnResult(responseHandlerClass("success", "未登入", {}, ''))

        except Exception as e:
            result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
    
    statusResult = httpStatusHandler.returnHttpStatus(result["status"])
    return JsonResponse(result, status=statusResult)

def updateMemberInfo(request):
    if request.method == "POST": 
        validatorResult = UserValidator.updateMemberInfoValidator(request)

        if(validatorResult != None):
            result = responseHandlerClass.returnResult(responseHandlerClass("typeError", "更新會員資料驗證錯誤", validatorResult, ''))
        
        else:
            try:
                if UserService.isLogin(request) == True:
                    UserService.updateUserInfo(request)

                    result = responseHandlerClass.returnResult(responseHandlerClass("success", "更新會員資訊", {}, ''))
                else:
                    result = responseHandlerClass.returnResult(responseHandlerClass("success", "未登入", {}, ''))

            except Exception as e:
                result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
    
        statusResult = httpStatusHandler.returnHttpStatus(result["status"])
        return JsonResponse(result, status=statusResult)

def forgetPassword(request):
    if request.method == "POST": 
        validatorResult = UserValidator.forgetPasswordValidator(request)

        if(validatorResult != None):
            result = responseHandlerClass.returnResult(responseHandlerClass("typeError", "忘記密碼驗證錯誤", validatorResult, ''))

        else:
            try:
                if UserService.isLogin(request) == True:
                    check_account = UserService.checkAccountBySession(request)

                    if check_account is None:
                        UserService.updateUserPassword(request)

                        result = responseHandlerClass.returnResult(responseHandlerClass("success", "密碼相同", {}, ''))
                    else:
                        result = responseHandlerClass.returnResult(responseHandlerClass("success", "更新會員密碼", {}, ''))
                else:
                    result = responseHandlerClass.returnResult(responseHandlerClass("success", "未登入", {}, ''))
                
            except Exception as e:
                result = responseHandlerClass.returnResult(responseHandlerClass("fail", "系統錯誤", {}, e))
    
        statusResult = httpStatusHandler.returnHttpStatus(result["status"])
        return JsonResponse(result, status=statusResult)
    
    