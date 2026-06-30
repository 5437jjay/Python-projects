def counter(f):
    count=0
    with open (f) as file:
        for line in file:
            if line.strip():
                count=count+1
    return count
def main():
    f=input("Enter the file name to open:")
    print("Number of lines of contents in the file named",f,"is",counter(f))
main()
