# Coke Machine Due Calculator
def main():
    try:
        a=int(input("Enter the number of coke bottles you've bought:"))
        coke(a)
    except ValueError:
        print("Invalid quantity\nPlease enter valid quantity in numbers")
    
def coke(b):
    a=b*50
    print("Hello Customer, We accept coins in 25 cents,10 cents and 5 cents ")
    while(a!=0):
        print("Amount Due:",a)
        i=int(input("Insert coin: "))
        if(i==5 or i==10 or i==25):
            a=a-i
        else:
            print("Enter  a valid coin...")
    else:
        print("Change Owed:",a )

main()