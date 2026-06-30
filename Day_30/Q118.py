books = []

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    status = "Available"
    books.append([book_id, title, author, status])
    print("Book added successfully.")

def display_books():
    if not books:
        print("No books found.")
        return
    print(f"{'ID':<8}{'Title':<25}{'Author':<20}{'Status':<10}")
    for b in books:
        print(f"{b[0]:<8}{b[1]:<25}{b[2]:<20}{b[3]:<10}")

def search_book():
    title = input("Enter Title to search: ")
    for b in books:
        if b[1].lower() == title.lower():
            print(f"Found: ID: {b[0]}, Title: {b[1]}, Author: {b[2]}, Status: {b[3]}")
            return
    print("Book not found.")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for b in books:
        if b[0] == book_id:
            if b[3] == "Available":
                b[3] = "Issued"
                print("Book issued successfully.")
            else:
                print("Book already issued.")
            return
    print("Book not found.")

def return_book():
    book_id = input("Enter Book ID to return: ")
    for b in books:
        if b[0] == book_id:
            if b[3] == "Issued":
                b[3] = "Available"
                print("Book returned successfully.")
            else:
                print("Book was not issued.")
            return
    print("Book not found.")

def delete_book():
    book_id = input("Enter Book ID to delete: ")
    for b in books:
        if b[0] == book_id:
            books.remove(b)
            print("Book deleted.")
            return
    print("Book not found.")

def menu():
    while True:
        print("\n--- Mini Library System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            display_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            issue_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

menu()