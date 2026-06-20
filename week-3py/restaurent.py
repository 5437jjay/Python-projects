# A program that acts like a restaurant menu and takes orders from the user. It should display the total cost of the order at the end.
def main():
    print("Welcome to our restaurant!")
    print("Here is our menu:")
    menu={
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
    }
    print(menu)
    order(menu)
def order(menu):  
        print("Please enter the items you would like to order (type 'done' when finished):")
        total=0.0
        while True:
            try:
                item=input("Item:")
                if item.lower() == 'done':
                    break
                total+=menu[item.lower()]
            except KeyError:
                    print("Item not found in the menu. Please enter a valid item.")
        print("Your total order cost is: $", round(total, 2))
main()