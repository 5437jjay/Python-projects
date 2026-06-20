import random
def guess():
    count=0
    print("Welcome to the Number Guessing Game!...")
    a=int(input("Enter the difficulty level between 1 to 100:"))
    print("Level: ",a)
    n=random.randint(1,a)
    while(True):
        try:
            
            g=int(input("Guess!:"))
            if(g<0):
                print("Nope!,It's not negative...")
                continue
            if(g<n):
                count=count+1
                print("Too Small!")
                continue
            elif(g>n):
                count=count+1
                print("Too Large!")
                continue
            elif(g==n):
                count=count+1
                print("Yeah!, perfectly Right!!")
                break

        except ValueError:
            print("Invalid input")
            continue
    print("Congratulations!,You've scored",a-count,"points Out of",a)
guess()
