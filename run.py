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

def retrievePswd(accountName):
    return Credentials.locateAccount(accName)

def retrieveAccName
