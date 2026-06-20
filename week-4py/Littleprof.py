import random
def prof():
    count=0
    try:
        dif=int(input("Enter the Difficulty Level:"))
        if(dif<0):
            print("The difficulty Level can't be negative")
        else:
            a=random.randint(0,dif)
            b=random.randint(0,dif)
            c=random.choice(["+","-","*","/"])
            while True:
                print(a,c,b,"=")
                print("Round your answers to two decimal places")
                ans=float(input("Enter your answer:"))
                if c is "+":
                    if(ans==a+b):
                        print("You're right!!!")
                        break
                    else:
                        print("Wrong answer")
                        count=count+1
                        continue
                    if(count==3):
                        print("The answer is:",round(a+b,2))
                if c is "-":
                    if(ans==a-b):
                        print("You're right!!!")
                        break
                    else:
                        print("Wrong answer")
                        count=count+1
                        continue
                    if(count==3):
                        print("The answer is:",round(a-b,2))
                if c is "*":
                    if(ans==a*b):
                        print("You're right!!!")
                        break
                    else:
                        print("Wrong answer")
                        count=count+1
                        continue
                    if(count==3):
                        print("The answer is:",round(a*b,2))
                if c is "/":
                    if(ans==a/b):
                        print("You're right!!!")
                        break
                    else:
                        print("Wrong answer")
                        count=count+1
                        continue
                    if(count==3):
                        print("The answer is:",round(a/b,2))
    except ValueError:
        print("Enter difficulty levels in formats like 1,2,..")
        prof()
prof()
