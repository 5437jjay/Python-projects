# Camel case to snake case converter
def main():
    camel_case=input("Enter a camel case string: ")
    camel_to_snake(camel_case)
def camel_to_snake(camel_case):
        for i in camel_case:
            print("_",i.lower(),sep="",end="")if i.isupper() else print(i,sep="",end="")
main()

    