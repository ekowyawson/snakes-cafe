#!/bin/python

def print_menu(menu):
    for category, items in menu.items():
        print(category)
        print("-" * len(category))
        for item in items:
            print(item)
        print()

def summarize_order(orders):
    print("\nYour order summary:")
    for item, qty in orders.items():
        print(f"- {qty} order{'s' if qty > 1 else ''} of {item}")
    print()

def main():
    menu = {
        "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
        "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
        "Desserts": ["Ice Cream", "Cake", "Pie"],
        "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
    }

    orders = {}

    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("*                                    *")
    print("** To quit at any time, type \"quit\" **")
    print("**************************************\n")

    print_menu(menu)

    print("*******************************************")
    print("**     What would you like to order?     **")
    print("**  To finish your order, type \"finish\"  **")
    print("*******************************************")
    
    while True:
        order = input("> ")

        if order.lower() == "quit":
            break

        if order.lower() == "finish":
            summarize_order(orders)
            break

        if order in menu['Appetizers'] + menu['Entrees'] + menu['Desserts'] + menu['Drinks']:
            orders[order] = orders.get(order, 0) + 1
            print(f"** {orders[order]} order{'s' if orders[order] > 1 else ''} of {order} have been added to your meal **")
        else:
            print(f"** We don't have {order} on the menu. Please choose something else. **")

if __name__ == "__main__":
    main()
