from ast import Continue


def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user ,password =data.split("|")
            print("User:" + user + ", " + "Password:" + password)

def add():
    name=input("Enter your Name: ")
    password=input("Set Your Passwod: ")
    with open("password.txt","a") as f:
        f.write(name + "|" + password + "\n")

while True:
 mode=input("Wolud you like to add a new password or view the existing one (view ,add) and press q for quit: \n"
 ).lower()
 if mode=="q":
    break
 if mode=="view":
    view()
 elif mode=="add":
    add()
 else:
    Continue

