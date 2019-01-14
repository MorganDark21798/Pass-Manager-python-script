class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "198"
        self.passw = "ADMIN"
        Login.error = "Enter a valid user id and password"
        

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print ("Login successful")
        else:
            print (Login.error)
log = Login("", "")
logid = input("Enter your user ID: ")
logpass = input("Enter your password: ")
log.authenticate()


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (username, password) VALUES (%s, %s)"
val = [
  ('Peter', 'ADMIN1'),
  ('Amy', 'ADMIN2'),
  ('Hannah', 'ADMIN3'),
  ('Michael', 'ADMIN4'),
  ('Sandy', 'ADMIN5'),
  ('Betty', 'ADMIN6'),
  ('Richard', 'ADMIN7'),
  ('Susan', 'ADMIN8')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 
