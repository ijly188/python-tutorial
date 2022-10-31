from email.policy import default
import json

class responseHandlerClass:
    def __init__(self, status, message, data, e):
        self.status = status
        self.message = message
        self.data = data
        self.e = e
        self.result = {
            'status': status,
            'message': message,
            'data': data,
            'error': e
        }
        
    def returnResult(self):
        # 要在這邊後續做針對不同的 status 的 errorHandler
        return self.result

class httpStatusHandler:
    def returnHttpStatus(status):
        match status:
            case "success":
                return 200
            case "typeError":
                return 422
            case "fail":
                return 500
            case _:
                return 200
