# Tweeting Form or Shorten form of Words
def main():
    a=input("Input: ")
    short(a)
def short(a):
    for i in a:
        print(end="",sep="") if i in"AEIOUaeiou" else print(i,sep="",end="")
main()