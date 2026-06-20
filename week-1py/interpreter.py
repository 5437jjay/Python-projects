# An interpreter handing two inputs from the users and perform operations on +,-,*,/ and print the result.
a=input("Expression:")
if("+" in a):
    b,c=a.split("+")
    print(int(b)+ int(c))
elif("-" in a):
    b,c=a.split("-")
    print(int(b)- int(c))  
elif("*" in a):
    b,c=a.split("*")                
    print(int(b)* int(c))
elif("/" in a):
    b,c=a.split("/")
    print(int(b)/ int(c))
else:
    print("Not a valid expression!")