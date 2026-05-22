print("WELCOME!! HOPE YOU ARE DOING GREAT TODAY....")

name = input("Enter your name: ")

choice = input("LOGIN/SIGNUP? ")

if(choice == "login"):

    user = input("Enter your username: ")

    if(name == user):
        print("Login Successful")

    else:
        print("Wrong credentials")

elif(choice == "signup"):

    pas = input("Enter your password: ")

    if(len(pas) >= 12):
        print("Yeahhhh...That's Nice...")

    else:
        print("Enter more than or equal to 12 characters")

print("THANK YOU")