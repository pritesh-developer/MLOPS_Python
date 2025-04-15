from signup import *

class user:
    def __init_(self):
        self.id=0
        print("this is init")

    def menu(self):
        user_input = input("What do you want to do? (1: Signup , 2: Login)")
        print(type(user_input))
        if user_input == "1":
            print("you have selected signup")
            sup = signup()
            sup.validate()

    def userDetails(self):
        print("This is user details")


obj = user()
obj.menu()