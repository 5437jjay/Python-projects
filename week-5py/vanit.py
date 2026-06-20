# Vanityplate Number Checker
def main():
    plate=input("Plate Number:")
    if(is_valid(plate)):
        print("Valid...")
    else:
        print("Invalid...")
def is_valid(p):
    a,b,c,d=0,0,0,1
    if(p.isalnum()):
        a=1
    if(p[0].isalpha() and p[1].isalpha()):
        b=1
    if(len(p)<=6):
        c=1
    for i in range(len(p)):
        if p[i].isdigit():
                if(p[i]=='0'):
                    d=0
                    break
                if(not p[i:].isdigit()):
                        d=0
                        break

    if((a and b and c and d)==1):
        return True
    else:
        return False

main()    