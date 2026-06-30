import csv
def data():
    print("Hi! User")
    print("We are here to help you in building a menu for your restaurent:")
    print("Make sure the first row is full field names and components")
    r=int(input("Enter the number of rows:"))
    c=int(input("Enter the number of columns:"))
    f=input("Enter the file name to have some backup of data:")
    if(".csv" not in f):
        print("We accept only .csv files")
        exit(1)
    file=open("1.csv","w")
    writer=csv.writer(file)
    i=0
    menu_list=[]
    while(i<r):
        print("Enter the menu items in row:",i+1)
        print("Note:Just separate fields by adding spaces in between the columns like pizza big small .. which comes under the same row but different columns")
        r_l=input().split(" ")
        if(len(r_l)<=c):    
            menu_list.append(r_l)
            writer.writerow(r_l)
            i=i+1
        else:
            print("You can't exceed number of items beyond the limit of number of columns of number of columns")
            i=0
            continue
    return(menu_list)
def table():
    from tabulate import tabulate
    print(tabulate(data()))
table()