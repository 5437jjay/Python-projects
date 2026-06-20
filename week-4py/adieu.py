def good():
    list1=["Adieu, ","adieu, ","to"]
    while(True):
        try:
            a=input("Name:")
            list1.append(a)
        except EOFError:
            break
    return list1
def main():
    a=good()
    n=len(a)
    a.insert(n-1,"and")
    n=len(a)
    for i in a:
        print(i,end=" ")
    

main()
