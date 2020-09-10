class Credentials:
    #Defining a list that will contain all user credentials
    credList=[]
   
    def save_credentials(self):
        Credentials.credList.append(self)
    
    def rub_credentials(self):
        Credentials.credList.remove(self)

    def __init__ (self, username,accountName,accountPassword):
        self.id=id
        self.username=username
        self.accountName=accountName
        self.accountPassword=accountPassword

    @classmethod
    def locateAccount(allCreds, acc_name):
        for cred in allCreds.credList:
            if cred.accountName==acc_name:
                return cred.accountPassword
    
    @classmethod 
    def show_cred(allCreds):
        return allCreds.credList
    
    @classmethod
    def available_creds(allCreds,acc_name):
        for cred in allCreds.credList:
            if cred.accountName==acc_name:
                 return True
    
        return False
   