"""
1)Create a Login class.
Use a private variable password.
Methods:
set_password(password)
login(input_password)
Rules:
Password must be at least 6 characters
Password should not be accessed directly
If password is correct, print Login successful
Else print Invalid password
"""
class Login:
    def __init__(self, password):
        if len(password) >= 6:
            self.__password = password
        else:
            print("Password should be at least of 6 characters")
            self.__password = None
    def set_password(self, new_password):
        if len(new_password) >= 6:
            self.__password = new_password
        else:
            print("Password should be at least of 6 characters")
    def input_password(self, input_password):
        if self.__password == input_password:
            print("Login successful")
        else:
            print("Invalid password")
obj = Login("User123")
obj.set_password("User123")
obj.input_password("User123")

"""
2) Create a StudentProfile class.
Use a private variable email.
Methods:
set_email(email)
get_email()
Rules:
Email must contain @
Email should not be accessed directly
If email is invalid, print Invalid email
"""
class StudentProfile:
    def __init__(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Email must contain @")
            self.__email = None
    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Email must contain @")
    def get_email(self):
        return self.__email
riyaa = StudentProfile("riyaa@gmail.com")
print(riyaa.get_email())
riyaa.set_email("riyaa@gmail.com")
print(riyaa.get_email())
"""
3) Create a User class.
Use a protected variable username.
Methods:
set_username(name)
get_username()
Create a child class Admin that accesses the protected variable.
Rules:
username should be accessed only inside the class or child class
Do not access it directly using object
"""
class User:
    def __init__(self, username):
        self._username = username
    def set_username(self, name):
        self._username = name
    def get_username(self):
        return self._username
class Admin(User):
    def check_username(self, name):
        if self._username == name:
            print("Valid username")
        else:
            print("Invalid username")
obj = Admin("riyaa")
print(obj.get_username())
obj.check_username("riya")