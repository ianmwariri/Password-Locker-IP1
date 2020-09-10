from user import User, Credentials
import random, string

def nuUser(username, signInPassword):
    nuUser=User(username,signInPassword)
    return nuUser

def saveAccount(user):
    user.signUpUser()
