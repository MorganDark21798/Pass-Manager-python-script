def askUser():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    checkPass(username, password)

def checkPass(use, pwd):
    if use == ("ID8") and pwd == ("admin"):
        login(use)
    else:
        print ("Your username and/or password was incorrect")
        askUser()

def login(use):
    print ("Welcome " + use)
    print ("You have successfully logged in!")
    askCom()

def askCom():
    command = input("Enter your command: ")
    if command == ("log off") or command == ("quit"):
        username = ("")
        password = ("")
        print ("You have logged off")
        askUser()
    if command == ("what is this code?") :
        username = ("")
        password = ("")
        print ("Python 3")
        askUser()
    else:
        print ("Unknown command")
        askCom()

askUser()
