# Define the menu of the restaurant
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 80,
    "Coffee": 55,
    "Coke": 30,
    }

print("Welcome to our restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: tk{price}")

order_total = 0

# First item
item_1 = input("Enter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, the item {item_1} is not available.")

# Option to order another item
another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Sorry, the item {item_2} is not available.")

# Print the total
print(f"The total amount you have to pay is: tk{order_total}")
