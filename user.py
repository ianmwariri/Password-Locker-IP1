class Credentials:
    #Defining a list that will contain all user credentials
    cred_list=[]
   
    def save_credentials(self):
        Credentials.cred_list.append(self)
    
    def rub_credentials(self):
        Credentials.cred_list.remove(self)

    def __init__ (self, username,accountName,accountPassword)
        self.id=id
        self.username=username
        self.accountName=accountName
        self.accountPassword=accountPassword

    @classmethod
    def locateAccount(allCreds, acc_name):
        for cred in allCreds.cred_list:
            if cred.accountName==acc_name:
                return cred.accountPassword
    
   