inventory = {}

def add_item():
    item_id = input("Enter item ID: ")
    if item_id in inventory:
        print("Item ID already exists")
        return
    name = input("Enter item name: ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
    except ValueError:
        print("Invalid quantity or price")
        return
    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    print("Item added successfully")

def view_items():
    if not inventory:
        print("Inventory is empty")
        return
    print(f"{'ID':<10}{'Name':<20}{'Quantity':<10}{'Price':<10}{'Total':<10}")
    for item_id, details in inventory.items():
        total = details['quantity'] * details['price']
        print(f"{item_id:<10}{details['name']:<20}{details['quantity']:<10}{details['price']:<10.2f}{total:<10.2f}")

def update_item():
    item_id = input("Enter item ID to update: ")
    if item_id not in inventory:
        print("Item not found")
        return
    print("Leave field blank to keep current value")
    name = input(f"Enter new name [{inventory[item_id]['name']}]: ")
    quantity = input(f"Enter new quantity [{inventory[item_id]['quantity']}]: ")
    price = input(f"Enter new price [{inventory[item_id]['price']}]: ")

    if name.strip() != "":
        inventory[item_id]['name'] = name
    if quantity.strip() != "":
        try:
            inventory[item_id]['quantity'] = int(quantity)
        except ValueError:
            print("Invalid quantity, keeping old value")
    if price.strip() != "":
        try:
            inventory[item_id]['price'] = float(price)
        except ValueError:
            print("Invalid price, keeping old value")
    print("Item updated successfully")

def delete_item():
    item_id = input("Enter item ID to delete: ")
    if item_id in inventory:
        del inventory[item_id]
        print("Item deleted successfully")
    else:
        print("Item not found")

def search_item():
    item_id = input("Enter item ID to search: ")
    if item_id in inventory:
        details = inventory[item_id]
        print(f"ID: {item_id}")
        print(f"Name: {details['name']}")
        print(f"Quantity: {details['quantity']}")
        print(f"Price: {details['price']}")
    else:
        print("Item not found")

def low_stock_report():
    try:
        threshold = int(input("Enter stock threshold: "))
    except ValueError:
        print("Invalid threshold")
        return
    found = False
    for item_id, details in inventory.items():
        if details['quantity'] < threshold:
            print(f"{item_id} - {details['name']} - Quantity: {details['quantity']}")
            found = True
    if not found:
        print("No items below threshold")

def total_inventory_value():
    total = sum(details['quantity'] * details['price'] for details in inventory.values())
    print(f"Total inventory value: {total:.2f}")

def main():
    while True:
        print("\n----- Inventory Management System -----")
        print("1. Add Item")
        print("2. View All Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Low Stock Report")
        print("7. Total Inventory Value")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            search_item()
        elif choice == '6':
            low_stock_report()
        elif choice == '7':
            total_inventory_value()
        elif choice == '8':
            print("Exiting Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()