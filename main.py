menu = {
    "Burger": 60,
    "Pizza": 99,
    "Pasta": 80,
    "Salad": 30,
    "Fries": 45,
    "Sandwich": 40,
    "Soup": 30,
    "Ice Cream": 30,
    "Coffee": 55,
    "Tea": 40,
}

orders = []

def display_menu():
    """Displays the menu with items and prices."""
    print("\n+------------+--------+")
    print("| Item       | Price  |")
    print("+------------+--------+")
    for item, price in menu.items():
        print(f"| {item:<10} | ${price:5.2f} |")
    print("+------------+--------+")

def take_order():
    """Allows the user to take orders from the menu."""
    global orders
    while True:
        display_menu()
        item = input("Enter the name of the item you want to order (or type 'done' to finish): ").strip().lower()
        if item == 'done':
            break
        new_item = item.title()
        if new_item in menu:
            orders.append(new_item)
            print(f"{new_item} has been added to your order.")
        else:
            print("Item not available. Please select from the menu.")

def display_order():
    """Displays the items in the order and calculates the total."""
    if not orders:
        print("\nNo items ordered.")
        return

    print("\nYour Order:")
    total = 0
    for item in orders:
        price = menu[item]
        total += price
        print(f"{item}: ${price:.2f}")
    print(f"Total: ${total:.2f}")

def main():
    """Main function for the food ordering system."""
    while True:
        print("\nWelcome to the Food Ordering System")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Display Order")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_menu()
        elif choice == "2":
            take_order()
        elif choice == "3":
            display_order()
        elif choice == "4":
            print("Thank you for using our Food Ordering System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
