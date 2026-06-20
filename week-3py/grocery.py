# A grocery list acts like a notes
def main():
    print("Enter the items you want to add to your grocery list (type 'done' when finished):")
    groc()
def groc():
    list=[]
    while True:
        a=input()
        if a.lower() == 'done':
            break
        if a.capitalize() not in list:
            list.append(a.capitalize())
    print("Your grocery list:")
    for item in list:
        print("- " + item)
main()