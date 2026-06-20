# A federal Bank's offer at early 1860's
def main():
    greet=input("Greeting:")
    print("Congratulations! You have won",Luckydraw(greet),"$")
def Luckydraw(greet):
    if(greet=="Hello" or greet=="hello"):
        return 100
    elif('h' == greet[0] or 'H' == greet[0]):
        return 20
    else:
        return 0
if __name__=="__main__":
    main()
