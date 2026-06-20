# A Fuel Gauge application which indicates how much fuel is in a tank.
def main():
    try:
        x=int(input("Enter the value of x :"))
        y=int(input("Enter the value of y :"))
        fuel(x,y)
    except ValueError:
        print("X and Y accept only integers\nEnter proper integers:")
        main()
def fuel(x,y):
    if(x<0 or y<0):
        print("x and y should be positive")
        main()
    else:
        try:
            c=x/y
            f=round(c,2)
            print("The tank is:",f*100,"%","full")
            if(f*100 == 99):
                print("The Tank is upto fill completely")
            elif(f*100 == 1):
                print("Fill the Tank immediately because your tank is almost empty")
        except ZeroDivisionError:
            print("The value of y should be non-negative")
            main()
main()
        
            