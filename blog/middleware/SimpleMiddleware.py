from django.http import Http404, HttpResponse, HttpResponseForbidden
import logging
from blog.service.user import UserService

logger = logging.getLogger('django')

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.warning('initialize')
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # logger.warning('1.get_response之前')
        response = self.get_response(request)
        # logger.warning('4.get_response之後')
        account = UserService.getUserInfoBySession(request)[0]["account"]
        requestMethod = request.method
        requestPath = request.path
        responseStatusCode = str(response.status_code)
        accessMsg = 'accessLog: ' + account + ' ' + requestMethod + ' ' + requestPath + ' ' + responseStatusCode
        logger.info( accessMsg )
        # Code to be executed for each request/response after
        # the view is called.
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # process_view() is called just before Django calls the view.
        # It should return either None or an HttpResponse object
        # 若返回None，則繼續處理request並往下執行適當的view。
        # 若返回HttpResponse，則不用多花時間調用其他view，直接應用。
        # print('request:', type(request), request)
        # print('request:', type(request.user.is_authenticated), request.user.is_authenticated)
        path = request.path
        isLogin = request.user.is_authenticated
        authList = [
            '/blog/member-info',
            '/blog/member-update'
        ]

        if path in authList:
            if isLogin == False:
                print("尼沒有驗證")
                return HttpResponseForbidden()

        # logger.warning('2. between req and res')
        return None

    def process_exception(self, request, exception):
        # Django calls process_exception() when a view raises an exception.
        # process_exception() should return either None or an HttpResponse object.
        logger.warning('---- exception.args ----')
        return None

    def process_template_response(self, request, response):
        # return TemplateResponse object(render相關)
        # logger.warning('3. view之後 ')
        return response