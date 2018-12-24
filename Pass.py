class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "198"
        self.passw = "ADMIN"
        Login.error = "Enter a valid user id and password"
        

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print ("Login successful")
            print ("Pass Manager v1")
    
        else:
            print (Login.error)
log = Login("", "")
logid = input("Enter your user ID: ")
logpass = input("Enter your password: ")
log.authenticate()

usrinput = input("Enter the social account: ")
if (usrinput == "fb"):
    print ("Your Password for Facebook is = *****")
if (usrinput == "t"):
    print ("Your Password for Twitter is = *****")
if (usrinput == "g"):
    print ("Your Password for Gmail is = *****")
else:
    print("error not reconized social account")
