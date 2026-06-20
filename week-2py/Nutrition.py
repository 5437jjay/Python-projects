def calorie():
    cal={"apple":130, "banana":105, "orange":85, "strawberry":50, "grapefruit":85, "kiwi":90, "pineapple":50, "mango":135, "papaya":120, "watermelon":80, "peach":60, "pear":100, "plum":30, "blueberry":85, "raspberry":65, "blackberry":70, "avocado":160, "coconut":150, "fig":40, "grape":60}
    a=input("Enter the name of the fruit: ")
    a=a.lower()
    if a in cal.keys():
        print("Calories in",a,"is",cal[a])
    else:
        print("Sorry, we don't have information on that fruit.")
calorie()