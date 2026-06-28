class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.next_book_id = 1
        self.next_member_id = 1

    def add_book(self, title, author, copies):
        book = Book(self.next_book_id, title, author, copies)
        self.books[self.next_book_id] = book
        self.next_book_id += 1
        return book.book_id

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def register_member(self, name):
        member = Member(self.next_member_id, name)
        self.members[self.next_member_id] = member
        self.next_member_id += 1
        return member.member_id

    def issue_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            return False
        book = self.books[book_id]
        member = self.members[member_id]
        if book.copies <= 0:
            return False
        book.copies -= 1
        member.borrowed_books.append(book_id)
        return True

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.books:
            return False
        member = self.members[member_id]
        if book_id not in member.borrowed_books:
            return False
        member.borrowed_books.remove(book_id)
        self.books[book_id].copies += 1
        return True

    def search_by_title(self, title):
        return [b for b in self.books.values() if title.lower() in b.title.lower()]

    def search_by_author(self, author):
        return [b for b in self.books.values() if author.lower() in b.author.lower()]

    def list_books(self):
        return list(self.books.values())

    def list_members(self):
        return list(self.members.values())


def display_book(book):
    print(f"ID: {book.book_id} | Title: {book.title} | Author: {book.author} | Copies: {book.copies}")


def display_member(member):
    print(f"ID: {member.member_id} | Name: {member.name} | Borrowed: {member.borrowed_books}")


def main():
    library = Library()
    while True:
        print("\n1. Add Book\n2. Remove Book\n3. Register Member\n4. Issue Book\n5. Return Book"
              "\n6. Search by Title\n7. Search by Author\n8. List Books\n9. List Members\n10. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            copies = int(input("Copies: "))
            book_id = library.add_book(title, author, copies)
            print(f"Book added with ID {book_id}")

        elif choice == "2":
            book_id = int(input("Book ID: "))
            if library.remove_book(book_id):
                print("Book removed")
            else:
                print("Book not found")

        elif choice == "3":
            name = input("Member name: ")
            member_id = library.register_member(name)
            print(f"Member registered with ID {member_id}")

        elif choice == "4":
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            if library.issue_book(member_id, book_id):
                print("Book issued")
            else:
                print("Could not issue book")

        elif choice == "5":
            member_id = int(input("Member ID: "))
            book_id = int(input("Book ID: "))
            if library.return_book(member_id, book_id):
                print("Book returned")
            else:
                print("Could not return book")

        elif choice == "6":
            title = input("Title: ")
            results = library.search_by_title(title)
            for b in results:
                display_book(b)

        elif choice == "7":
            author = input("Author: ")
            results = library.search_by_author(author)
            for b in results:
                display_book(b)

        elif choice == "8":
            for b in library.list_books():
                display_book(b)

        elif choice == "9":
            for m in library.list_members():
                display_member(m)

        elif choice == "10":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()