from user import User, Credentials
import random, string

def nuUser(username, signInPassword):
    nuUser=User(username,signInPassword)
    return nuUser

def saveAccount(user):
    user.signUpUser()

def authentication(username,signInPassword):
    return User.userLoginAuthentication(username, signInPassword)

def nuCreds(username,accountName,accountPassword):
    nuCreds=Credentials(username,accountName,accountPassword)
    return nuCreds

def storeCreds(cred):
    cred.storeCreds()

def rubCred(accName):
    Credentials.rubCred(accName)

def retrieveAccPswd(accName):
    return Credentials.locateAccount(accName)

def retrieveAccName(accName):
    return Credentials.locateName(accName)

def showCred(accName):
    return Credentials.availableCreds(accName)

def locateCred(accName):
    return Credentials.availableCreds(accName)

def showCreds():
    return Credentials.showCred()

def generatePswd(length):
    pswdsList=[]
    counter=1
    while counter<=length:
        randomisePswd=random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
        pswdsList.append(randomisePswd)
        counter+=1
    return "".join(pswdsList)

