class Contact:
    def __init__(self, contact_id, name, phone, email, address):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.next_id = 1

    def add_contact(self, name, phone, email, address):
        contact = Contact(self.next_id, name, phone, email, address)
        self.contacts[self.next_id] = contact
        self.next_id += 1
        return contact.contact_id

    def update_contact(self, contact_id, name=None, phone=None, email=None, address=None):
        if contact_id not in self.contacts:
            return False
        contact = self.contacts[contact_id]
        if name:
            contact.name = name
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if address:
            contact.address = address
        return True

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            return True
        return False

    def search_by_name(self, name):
        return [c for c in self.contacts.values() if name.lower() in c.name.lower()]

    def search_by_phone(self, phone):
        return [c for c in self.contacts.values() if phone in c.phone]

    def list_contacts(self):
        return list(self.contacts.values())


def display_contact(contact):
    print(f"ID: {contact.contact_id} | Name: {contact.name} | Phone: {contact.phone} | Email: {contact.email} | Address: {contact.address}")


def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact\n2. Update Contact\n3. Delete Contact\n4. Search by Name"
              "\n5. Search by Phone\n6. List Contacts\n7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact_id = manager.add_contact(name, phone, email, address)
            print(f"Contact added with ID {contact_id}")

        elif choice == "2":
            contact_id = int(input("Contact ID: "))
            name = input("New name (leave blank to skip): ")
            phone = input("New phone (leave blank to skip): ")
            email = input("New email (leave blank to skip): ")
            address = input("New address (leave blank to skip): ")
            if manager.update_contact(contact_id, name or None, phone or None, email or None, address or None):
                print("Contact updated")
            else:
                print("Contact not found")

        elif choice == "3":
            contact_id = int(input("Contact ID: "))
            if manager.delete_contact(contact_id):
                print("Contact deleted")
            else:
                print("Contact not found")

        elif choice == "4":
            name = input("Name: ")
            results = manager.search_by_name(name)
            for c in results:
                display_contact(c)

        elif choice == "5":
            phone = input("Phone: ")
            results = manager.search_by_phone(phone)
            for c in results:
                display_contact(c)

        elif choice == "6":
            for c in manager.list_contacts():
                display_contact(c)

        elif choice == "7":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()