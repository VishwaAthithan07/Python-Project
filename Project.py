import json

inventory = {}
inventory_file = "inventory.json"


def save_inventory():
    f = open(inventory_file, "w")
    json.dump(inventory, f)
    f.close()


def load_inventory():
    f = open(inventory_file, "a+")
    f.seek(0)
    data = f.read()
    if data != "":
        global inventory
        inventory = json.loads(data)
    f.close()


def add_item():
    load_inventory()
    item_id = input("Enter item ID: ")
    name = input("Enter name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    save_inventory()
    print("Item added!")


def update_item():
    load_inventory()
    item_id = input("Enter ID to update: ")
    if item_id in inventory:
        quantity = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[item_id]["quantity"] = quantity
        inventory[item_id]["price"] = price
        save_inventory()
        print("Item updated!")
    else:
        print("Item not found.")


def remove_item():
    load_inventory()
    ids = input("Enter one or more IDs to remove (comma separated): ")
    id_list = ids.split(",")
    removed = False

    for item_id in id_list:
        item_id = item_id.strip()
        if item_id in inventory:
            del inventory[item_id]
            removed = True
            print(f"Removed: {item_id}")
        else:
            print(f"Item not found: {item_id}")

    if removed:
        save_inventory()
    else:
        print("No items removed.")


def search_item():
    load_inventory()
    item_id = input("Enter ID to search: ")
    if item_id in inventory:
        item = inventory[item_id]
        print("\n--- Item Found ---")
        print("ID:", item_id)
        print("Name:", item["name"])
        print("Quantity:", item["quantity"])
        print("Price:", item["price"])
        print("------------------")
    else:
        print("Item not found.")


def list_inventory():
    load_inventory()
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\n--- INVENTORY LIST ---")
        # print header
        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Price':<10}")
        print("-" * 50)
        # print each item in a formatted row
        for key in inventory:
            item = inventory[key]
            print(f"{key:<10} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f}")
        print("-" * 50)


def admin_menu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Add item")
        print("2. Update item")
        print("3. Remove item (multiple allowed)")
        print("4. Search item")
        print("5. List inventory")
        print("6. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            list_inventory()
        elif choice == "6":
            print("Logging out (Admin)...")
            break
        else:
            print("Invalid choice.")


def user_menu():
    while True:
        print("\n=== USER MENU ===")
        print("1. Search item")
        print("2. List inventory")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            search_item()
        elif choice == "2":
            list_inventory()
        elif choice == "3":
            print("Logging out (User)...")
            break
        else:
            print("Invalid choice.")


def main():
    load_inventory()
    while True:
        print("\n=== LOGIN ===")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == "admin" and password == "pass":
            admin_menu()
        else:
            user_menu()

        again = input("Type 'exit' to quit or press Enter to login again: ")
        if again.lower() == "exit":
            print("Exiting program...")
            break


main()
