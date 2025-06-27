inventory = {}

def add_item():
    item = input("Enter item name: ").capitalize()
    if item in inventory:
        print("Item already exists. Use update option instead.")
    else:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: $"))
        inventory[item] = {"quantity": qty, "price": price}
        print(f"{item} added successfully.")

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Inventory List ---")
    for item, details in inventory.items():
        print(f"{item}: Quantity = {details['quantity']}, Price = ${details['price']:.2f}")

def update_item():
    item = input("Enter item name to update: ").capitalize()
    if item in inventory:
        qty = int(input("Enter new quantity: "))
        price = float(input("Enter new price: $"))
        inventory[item]['quantity'] = qty
        inventory[item]['price'] = price
        print(f"{item} updated successfully.")
    else:
        print("Item not found.")

def delete_item():
    item = input("Enter item name to delete: ").capitalize()
    if item in inventory:
        del inventory[item]
        print(f"{item} deleted from inventory.")
    else:
        print("Item not found.")

def menu():
    while True:
        print("\n--- Inventory Management ---")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
menu()
