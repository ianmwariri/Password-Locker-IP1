import pyperclip

class Credentials:
    #Defining a list that will contain all user credentials
    credList=[]
   
    def storeCreds(self):
        Credentials.credList.append(self)
    
    def rubCreds(self):
        Credentials.credList.remove(self)

    def __init__ (self, username,accountName,accountPassword):
        self.id=id
        self.username=username
        self.accountName=accountName
        self.accountPassword=accountPassword

    @classmethod
    def locateAccount(cls, accName):

        for cred in cls.credList:
            if cred.accountName==accName:
                return cred.accountName
    
    @classmethod
    def locateName(cls, accName):
        for cred in cls.credList:
            if cred.accountName==accName:
                return cred.accountName


    @classmethod            
    def rubCred(cls,accName):
        for cred in cls.credList:
            if cred.accountName==accName:
                Credentials.rubCreds(cred)
    
    @classmethod 
    def show_cred(cls):
        return cls.credList
    
    @classmethod
    def available_creds(cls,accName):
        for cred in cls.credList:
            if cred.accountName==accName:
                 return True
    
        return False
   
    class User:

        userList=[]
        def signUpUser(self):

            User.userList.append(self)
        
        def __init__(self, username,signInPasswd):
            self.username=username
            self.signInPasswd=signInPasswd
        
        @classmethod
        def userLoginAuthentication(cls,username,authPassword):
            for user in cls.userList:
                if user.username==username and user.signInPasswd == authPassword:
                    return True
            return False


    