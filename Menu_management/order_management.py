# Define the menu of the restaurant
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 80,
    "Coffee": 55,
}

print("Welcome to our restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: tk{price}")

order_total = 0
ordered_items = []  # List to store ordered items and their prices

# First item
item_1 = input("Enter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total += menu[item_1]
    ordered_items.append((item_1, menu[item_1]))
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Sorry, the item '{item_1}' is not available.")

# Option to order another item
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        ordered_items.append((item_2, menu[item_2]))
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available.")

# Print the bill
print("\n--- Bill Receipt ---")
print("Item                Price")
print("-------------------------")
for item, price in ordered_items:
    print(f"{item:<20} tk{price}")
print("-------------------------")
print(f"Total Amount:       tk{order_total}")
print("-------------------------")
print("Thank you for dining with us!")
