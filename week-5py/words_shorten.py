import sys
def main():
    print("Enter the string or sequence of strings to be shorten:")
    name=sys.stdin.read()
# Once the inputs are entered press enter and then press Ctrl+z+enter
    print("The string after shorten is:",check(name))
def check(name):
    st=""
    for i in name:
        if(i in "AEIOUaeiou"):
            continue
        st=st+i
    return st
if __name__=="__main__":
    main()