import pickle as p 
import  foodadvicer
g=foodadvicer.foodgen()
from datetime import date
today = date.today()
f1=open("registerfood.dat","rb+")


def register():
    m={}
    print("Welcome to Adboy's Food Advicer")
    i=int(input("Are You a New Member \n 1.Yes \n 2.No \n Enter 1 or 2 :    "))
    x=True
    if i==1:
        
        m["email"]=input("enter email id ")
        password=input("Enter a valid password \n Length Should Be 8 or more \n  One digit is necessary\n One special character is necssary\n Enter Password :  ")
        m["password"]=password
        while x :

            if len(password)<8 or password.isalnum()==True :
                 print("please read the restrictions")
                 password=input("Enter a valid password \n Length Should Be 8 or more \n One digit is necessary\n One special character is necssary\n Enter Password :  ")
            else:
                x=False
            
                  
        else:
            print("succesfully registered")
            p.dump(m,f1)
            home()
            
            
    elif i==2:
        email=input("enter your email id ")
        pwd=input("Enter your Password ")
        try:
            f1.seek(0)
            while True:
                d=p.load(f1)
                if d["email"]==email and d["password"]==pwd:
                    print("Succesfull Login")
                    home()
                    break
                else:
                    print("User not found")
                    print("Please sign up again")
                    register()
        except:
           f1.close() 

    else:
        print("PLease enter a valid option")
        register() 
def home():
    print("Welcome to the food Advicer app")
    print("1.Morning Breakfast \n 2.Afternoon lunch\n 3.Snacks\n 4.Dinner\n 5.Exit\n")
    c=int(input("enter your option:  "))
    if c==1:
        x=g.morning()
        print(x)
    elif c==2:
        print("1.Curry\n 2.Sambar\n 3.Rasam")

        sad=int(input("Enter your option:  "))
        if sad==1:
            x=g.curry()
            print(x)
            home()
        elif sad==2:
            x=g.sambar()
            print(x)
            home()
        elif sad==3:
            x=g.rasam()
            print(x)
            home()
        else:
            home()
    elif c==3:
        x=g.snacks()
        print(x)
        home()
    elif c==4:
        x=g.dinnner()
        print(x)
        home()
    elif c==5:
        exit()
    else:
        print("Please enter a valid option")
        home()
register()



    