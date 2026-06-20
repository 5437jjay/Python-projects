# Conversion of Anno domini format to the standard format according to ISO 8601
def main():
    try:
        date=input("Enter the date in Anno Domini format (e.g. month|day|year): ")
        convert(date)
    except ValueError:
        print("Invalid date format. Please enter the date in the correct format.")
        main()
def convert(date):
    a,b,c=date.split("|")
    if len(a)<2:
        a="0"+a
    if len(b)<2:    
        b="0"+b
    try:
        if(int(a)<1 or int(a)>12):
            print("Invalid month. Please enter a month between 1 and 12.")
            main()
        elif(int(b)<1 or int(b)>31):
            print("Invalid day. Please enter a day between 1 and 31.")
            main()
        elif(int(c)<1):
            print("Invalid year. Please enter a valid year.")
            main()
        else:
            print("The date in ISO 8601 format is:", c+"-"+a+"-"+b)
    except ValueError:
        print("Invalid date format. Please enter the date in the correct format.")
        main()
main()
