students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append([roll, name, marks])
    print("Student added successfully.")

def display_students():
    if not students:
        print("No records found.")
        return
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
    for s in students:
        print(f"{s[0]:<10}{s[1]:<20}{s[2]:<10}")

def search_student():
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s[0] == roll:
            print(f"Found: Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")
            return
    print("Student not found.")

def update_student():
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s[0] == roll:
            s[1] = input("Enter new Name: ")
            s[2] = float(input("Enter new Marks: "))
            print("Record updated.")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s[0] == roll:
            students.remove(s)
            print("Record deleted.")
            return
    print("Student not found.")

def menu():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

menu()