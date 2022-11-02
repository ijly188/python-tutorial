import json
from blog.models import UserProfile
from blog.models import Article as ArticleModel
from blog.service.user import UserService as UserService

class ArticleService:
    def ArticleListByAccount(request):
        account = UserService.getUserInfoBySession(request)[0]["account"]
        user = UserProfile.objects.get(account=account)

        returnData = []
        returnDataElement = {}

        articleListQuerySet = ArticleModel.objects.filter(account=user)
        articleListData = list(articleListQuerySet)

        for article in articleListData:
            returnDataElement = {
                "id": article.id,
                "author": {
                    "article_id": article.account.id,
                    "last_login": article.account.last_login.strftime("%Y-%m-%d %H:%M:%S"),
                    "username": article.account.username,
                    "date_joined": article.account.date_joined.strftime("%Y-%m-%d %H:%M:%S"),
                    "account": article.account.account,
                    "email": article.account.email,
                    "first_name": article.account.first_name,
                    "last_name": article.account.last_name,
                    "phone": article.account.phone,
                    "create_time": article.account.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "update_time": article.account.update_time.strftime("%Y-%m-%d %H:%M:%S"),
                },
                "content": article.content,
                "create_time": article.create_time.strftime("%Y-%m-%d %H:%M:%S"),
                "last_edit_time": article.last_edit_update.strftime("%Y-%m-%d %H:%M:%S")
                
            }

            returnData.append(returnDataElement)

        return returnData

    def ArticleList(request):
        returnData = []
        returnDataElement = {}

        articleListQuerySet = ArticleModel.objects.all()
        articleListData = list(articleListQuerySet)

        for article in articleListData:
            returnDataElement = {
                "article_id": article.id,
                "author": article.account_id,
                "author": {
                    "article_id": article.account.id,
                    "last_login": article.account.last_login,
                    "username": article.account.username,
                    "date_joined": article.account.date_joined,
                    "account": article.account.account,
                    "email": article.account.email,
                    "first_name": article.account.first_name,
                    "last_name": article.account.last_name,
                    "phone": article.account.phone,
                    "create_time": article.account.create_time,
                    "update_time": article.account.update_time,
                },
                "content": article.content,
                "create_time": article.create_time,
                "last_edit_time": article.last_edit_update
            }
            returnData.append(returnDataElement);
        
        return returnData

    def createArticleByAccount(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        # 因為我們在建立 article model 的時候我們讓 account 要符合 userProfile 的 userModel 所以會很麻煩
        account = UserService.getUserInfoBySession(request)[0]["account"]
        user = UserProfile.objects.get(account=account)

        content = data["content"]

        article = ArticleModel.objects.create(
            account = user,
            content = content
        )
        
        returnArticleListById = ArticleService.ArticleListByAccount(request)

        return returnArticleListById
        

        
