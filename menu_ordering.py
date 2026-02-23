# Restaurant Menu Ordering System
menu = {
    "Burger":5.99,
    "Pizza": 8.99,
    "Pasta": 7.49,
    "Salad": 4.99,
    "Drink": 2.49
}

# Function to display the menu
def display_menu():
    print("Welcome to the Restaurant!")
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: {price:.2f}")
    print()

# Function to take orders
def take_order():
    order = {}
    while True:
        item = input("Enter the item you want to order (or 'done' to finish): ").strip().title()
        if item.lower() == 'done':
            break
        if item in menu:
            quantity = int(input(f"Enter quantity for {item}: "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Invalid item. Please choose from the menu.")
    return order

# Function to calculate total
def calculate_total(order):
    total = 0
    print("\nYour Order:")
    for item, quantity in order.items():
        price = menu[item]
        item_total = price * quantity
        print(f"{item} x{quantity}: ${item_total:.2f}")
        total += item_total
    print(f"Total: ${total:.2f}")
    return total

# Main function
def main():
    display_menu()
    order = take_order()
    if order:
        calculate_total(order)
    else:
        print("No items ordered.")

if __name__ == "__main__":
    main()
