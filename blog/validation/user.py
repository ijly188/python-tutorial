import json
import logging
from blog.validation.validator import validatorClass

logger = logging.getLogger('django')
class UserValidator:
    logger.debug('debug 紀錄此訊息')
    logger.info('info 紀錄此訊息')
    logger.warning('warning 紀錄此訊息')
    logger.error('error 紀錄此訊息')
    logger.critical('critical 紀錄此訊息')
    
    def registerValidator(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        resultList = {}

        account = data["account"]
        accountValidation = validatorClass.AccountValidation(account)
        if(accountValidation != []):
            resultList['accountError'] = accountValidation

        email = data["email"]
        emailValidation = validatorClass.EmailValidation(email)
        if(emailValidation != []):
            resultList['emailError'] = emailValidation

        first_name = data["first_name"]
        firstNameValidation = validatorClass.FirstNameValidation(first_name)
        if(firstNameValidation != []):
            resultList['firstNameError'] = firstNameValidation

        last_name = data["last_name"]
        lastNameValidation = validatorClass.LastNameValidation(last_name)
        if(lastNameValidation != []):
            resultList['lastNameError'] = lastNameValidation

        password = data["password"]
        passwordValidation = validatorClass.PasswordValidation(password)
        if(passwordValidation != []):
            resultList['passwordError'] = passwordValidation

        phone = data["phone"]
        phoneValidation = validatorClass.PhoneValidation(phone)
        if(phoneValidation != []):
            resultList['phoneError'] = phoneValidation


        if(resultList == {}):
            return None
        else:
            return resultList

    def loginValidator(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        resultList = {}

        account = data["account"]
        accountValidation = validatorClass.AccountValidation(account)
        if(accountValidation != []):
            resultList['accountError'] = accountValidation

        password = data["password"]
        passwordValidation = validatorClass.PasswordValidation(password)
        if(passwordValidation != []):
            resultList['passwordError'] = passwordValidation

        if(resultList == {}):
            return None
        else:
            return resultList

    def updateMemberInfoValidator(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        resultList = {}

        account = data["account"]
        accountValidation = validatorClass.AccountValidation(account)
        if(accountValidation != []):
            resultList['accountError'] = accountValidation

        email = data["email"]
        emailValidation = validatorClass.EmailValidation(email)
        if(emailValidation != []):
            resultList['emailError'] = emailValidation

        first_name = data["first_name"]
        firstNameValidation = validatorClass.FirstNameValidation(first_name)
        if(firstNameValidation != []):
            resultList['firstNameError'] = firstNameValidation

        last_name = data["last_name"]
        lastNameValidation = validatorClass.LastNameValidation(last_name)
        if(lastNameValidation != []):
            resultList['lastNameError'] = lastNameValidation

        phone = data["phone"]
        phoneValidation = validatorClass.PhoneValidation(phone)
        if(phoneValidation != []):
            resultList['phoneError'] = phoneValidation


        if(resultList == {}):
            return None
        else:
            return resultList
    
    def forgetPasswordValidator(request):
        data = json.loads(bytes.decode(request.body, "utf-8"))

        resultList = {}

        password = data["password"]
        passwordValidation = validatorClass.PasswordValidation(password)
        if(passwordValidation != []):
            resultList['passwordError'] = passwordValidation

        if(resultList == {}):
            return None
        else:
            return resultList