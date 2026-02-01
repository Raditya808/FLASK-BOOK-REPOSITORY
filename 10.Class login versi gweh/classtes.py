class lgtes(object):
    def __init__(self,username="",password=""):
        self.username = username
        self.password = password

    # untuk set di main.py   
    def setnama(self,username):
        self.username = username
    
    # return nama di kirim ke html sukses.html
    def dapat_nama(self):
        return self.username 
        
    # password 
    def setpassword(self,password):
        self.password = password

    #return password (TIDAK DI SARANKAN) karena saat di return password akan masuk
    #def dapat_password(self):
        #return self.password

    # return logic untuk login 
    def autentikasi(self):
        if self.username == 'radit' and self.password == '123':
            return True 
        else:
            return False

