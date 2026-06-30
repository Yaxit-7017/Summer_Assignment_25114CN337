contacts = []

def is_valid_name(name):
    return name.replace(" ", "").isalpha()

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact():
    name = input("Enter Name: ")
    if not is_valid_name(name):
        print("Invalid name. Only letters allowed.")
        return
    phone = input("Enter Phone Number: ")
    if not is_valid_phone(phone):
        print("Invalid phone number. Must be 10 digits.")
        return
    email = input("Enter Email: ")
    contacts.append([name.title(), phone, email.lower()])
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts found.")
        return
    sorted_contacts = sorted(contacts, key=lambda c: c[0])
    print(f"{'Name':<20}{'Phone':<15}{'Email':<25}")
    for c in sorted_contacts:
        print(f"{c[0]:<20}{c[1]:<15}{c[2]:<25}")

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for c in contacts:
        if keyword in c[0].lower() or keyword in c[1]:
            print(f"Found: Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    phone = input("Enter Phone Number of contact to update: ")
    for c in contacts:
        if c[1] == phone:
            new_name = input("Enter new Name: ")
            if is_valid_name(new_name):
                c[0] = new_name.title()
            c[2] = input("Enter new Email: ").lower()
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    phone = input("Enter Phone Number of contact to delete: ")
    for c in contacts:
        if c[1] == phone:
            contacts.remove(c)
            print("Contact deleted.")
            return
    print("Contact not found.")

def count_contacts():
    print(f"Total Contacts: {len(contacts)}")

def menu():
    while True:
        print("\n--- Mini Contact Book Project ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Count Contacts")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            count_contacts()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

menu()