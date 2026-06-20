# This program asks the user for the current time and determines whether it's breakfast, lunch, or dinner time.
def main():
    tim=input("What time is it?\nPlease enter the time in the format of H.M a.m or p.m (e.g., 7.30 a.m, 12:00 p.m): ")
    t,a=tim.split(" ")
    d=time(t)
    if("pm" in a.lower() or "p.m" in a.lower()):
           d=12+d    
    if(d>=7.0 and d<=8.0):
        print("breakfast time")
    elif(d>=12.0 and d<=13.0):
        print("lunch time")
    elif(d>=18.0 and d<=19.0):
        print("dinner time")
    else:
        print("Please Stick to your schedule!\nIt's not meal time!")
def time(t):
    if("." in t):
        h,m=t.split(".")
    elif(":" in t):
        h,m=t.split(":")
    else:
        print("Invalid time format!")
        return 0
    h=int(h)
    m=int(m)    
    time=h+(m/60)
    return time
main()
