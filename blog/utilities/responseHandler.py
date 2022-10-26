import json

class responseHandlerClass:
    def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = data
    
    def returnJSON(classObject):
        return json.dumps(classObject.__dict__)

class responseHandler:

    res = {
        "status": "",
        "message": "",
        "data": {}
    }

    def responseHandler(res):
        # 可以針對錯誤訊息做 log collection
        return res