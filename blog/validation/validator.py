import re

class validatorClass:
    # 後面可以想一下 validation 全部抽出去，連同下面判斷的方法一起出去
    # regex list
    emailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    telRegex = r'0(\d{1})-?\d{4}-?\d{4}'

    def AccountValidation(account):
        accountValidation = []

        # 驗證是不是為空
        isEmptyResult = validatorClass.isEmpty(account)
        if(isEmptyResult == True):
            accountValidation.append("帳號未輸入")
        
        # 驗證是否為字串
        isStringResult = validatorClass.isString(account)
        if(isStringResult == False):
            accountValidation.append("帳號輸入錯誤")


        return accountValidation
    
    def EmailValidation(email):
        emailValidation = []

        # 驗證不能為空
        isEmptyResult = validatorClass.isEmpty(email)
        if(isEmptyResult == True):
            emailValidation.append("信箱未輸入")

        # 驗證是否為信箱
        isEmailResult = validatorClass.isEmail(email)
        if(isEmailResult == False):
            emailValidation.append("信箱格式錯誤")

        return emailValidation
        
    def FirstNameValidation(firstName):
        firstNameValidation = []

        # 驗證是否為空
        isEmptyResult = validatorClass.isEmpty(firstName)
        if(isEmptyResult == True):
            firstNameValidation.append("未輸入姓氏")
        
        # 驗證是否為字串
        isStringResult = validatorClass.isString(firstName)
        if(isStringResult == False):
            firstNameValidation.append("姓氏輸入錯誤")
        
        return firstNameValidation
    
    def LastNameValidation(lastName):
        lastNameValidation = []

        # 驗證是否為空
        isEmptyResult = validatorClass.isEmpty(lastName)
        if(isEmptyResult == True):
            lastNameValidation.append("未輸入名字")
        
        # 驗證是否為字串
        isStringResult = validatorClass.isString(lastName)
        if(isStringResult == False):
            lastNameValidation.append("名字輸入錯誤")
        
        return lastNameValidation

    def PasswordValidation(password):
        passwordValidation = []

        # 驗證是否為空
        isEmptyResult = validatorClass.isEmpty(password)
        if(isEmptyResult == True):
            passwordValidation.append("未輸入密碼")
        
        # 驗證是否為字串
        isStringResult = validatorClass.isString(password)
        if(isStringResult == False):
            passwordValidation.append("密碼輸入錯誤")
        
        return passwordValidation

    def PhoneValidation(phone):
        # 先轉字串 不然用 int 去判的話會大爆炸
        phone = str(phone)
        phoneValidation = []

        # 驗證是否為空
        isEmptyResult = validatorClass.isEmpty(phone)
        if(isEmptyResult == True):
            phoneValidation.append("未輸入市話")
        
        # 驗證是否為市話
        isPhoneResult = validatorClass.isTelPhone(phone)
        if(isPhoneResult == False):
            phoneValidation.append("市話輸入錯誤")
        
        return phoneValidation


    def isEmpty(data):
        if(data == ''):
            return True
        else:
            return False

    def isString(data):
        if(str(type(data)) == "<class 'str'>"):
            return True
        else:
            return False

    def isEmail(data):
        if(re.fullmatch(validatorClass.emailRegex, data)):
            return True
        else:
            return False

    def isTelPhone(data):
        if(re.fullmatch(validatorClass.telRegex, data)):
            return True
        else:
            return False