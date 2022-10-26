import json
from blog.models import UserProfile

class UserService:
    def checkAccountExistByAccount(account):
        return UserProfile.objects.filter(account=account).first()
    
    def checkAccountPassword(account, password):
        return UserProfile.objects.filter(account=account, password=password).first()
    
    def checkSessionPassword(request, password):
        userId = UserService.getLoginUserId(request)

        return UserProfile.objects.filter(id=userId, password=password).first()

    def createUser(account, first_name, last_name, email, phone, password):
        user = UserProfile.objects.create_user(
            account = account,
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            username = account,
        )
        user.set_password(password)
        user.save()

    def updateUserInfo(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        account = data["account"]
        email = data["email"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        phone = data["phone"]

        userId = UserService.getLoginUserId(request)

        UserProfile.objects.filter(id=userId).update(
            account = account,
            email = email,
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            username = account,
        )
        
    def updateUserPassword(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))
        
        password = data["password"]
        userId = UserService.getLoginUserId(request)

        user = UserProfile.objects.filter(id=userId).first()
        user.set_password(password)
        user.save()

    def isLogin(request):
        return request.user.is_authenticated
    
    def getLoginUserId(request):
        return request.session.get('_auth_user_id')

    def getUserInfoBySession(request):
        userId = UserService.getLoginUserId(request)

        return UserProfile.objects.filter(id=userId).values()

    def getReturnUserInfoJson(request):
        memberInfo = list(UserService.getUserInfoBySession(request))[0]

        return {
            "account": memberInfo['account'],
            "username": memberInfo['username'],
            "email": memberInfo['email'],
            "first_name": memberInfo['first_name'],
            "last_name": memberInfo['last_name'],
            "phone": memberInfo['phone'],
            "last_login": memberInfo['last_login'].strftime("%Y-%m-%d %H:%M:%S"),
        }
