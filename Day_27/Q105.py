import os

FILE_NAME = "students.txt"

def load_records():
    records = []
    if not os.path.exists(FILE_NAME):
        return records

    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            roll_no, name, age, course, marks = line.split(",")
            records.append({
                "roll_no": roll_no,
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            })
    return records

def save_records(records):
    with open(FILE_NAME, "w") as f:
        for r in records:
            f.write(f"{r['roll_no']},{r['name']},{r['age']},{r['course']},{r['marks']}\n")

def add_student():
    records = load_records()

    roll_no = input("Enter Roll Number: ").strip()

    for r in records:
        if r["roll_no"] == roll_no:
            print("A student with this roll number already exists!\n")
            return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    marks = input("Enter Marks: ").strip()

    records.append({
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    })

    save_records(records)
    print("Student record added successfully!\n")

def view_students():
    records = load_records()

    if not records:
        print("No student records found.\n")
        return

    print("\n" + "-" * 70)
    print(f"{'Roll No':<10}{'Name':<20}{'Age':<6}{'Course':<15}{'Marks':<10}")
    print("-" * 70)
    for r in records:
        print(f"{r['roll_no']:<10}{r['name']:<20}{r['age']:<6}{r['course']:<15}{r['marks']:<10}")
    print("-" * 70 + "\n")

def search_student():
    records = load_records()
    roll_no = input("Enter Roll Number to search: ").strip()

    for r in records:
        if r["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Roll No : {r['roll_no']}")
            print(f"Name    : {r['name']}")
            print(f"Age     : {r['age']}")
            print(f"Course  : {r['course']}")
            print(f"Marks   : {r['marks']}\n")
            return

    print("No student found with that roll number.\n")

def update_student():
    records = load_records()
    roll_no = input("Enter Roll Number to update: ").strip()

    for r in records:
        if r["roll_no"] == roll_no:
            print("Leave a field blank to keep its current value.")

            name = input(f"Name [{r['name']}]: ").strip()
            age = input(f"Age [{r['age']}]: ").strip()
            course = input(f"Course [{r['course']}]: ").strip()
            marks = input(f"Marks [{r['marks']}]: ").strip()

            if name:
                r["name"] = name
            if age:
                r["age"] = age
            if course:
                r["course"] = course
            if marks:
                r["marks"] = marks

            save_records(records)
            print("Student record updated successfully!\n")
            return

    print("No student found with that roll number.\n")

def delete_student():
    records = load_records()
    roll_no = input("Enter Roll Number to delete: ").strip()

    for r in records:
        if r["roll_no"] == roll_no:
            confirm = input(f"Delete record of {r['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                records.remove(r)
                save_records(records)
                print("Student record deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    print("No student found with that roll number.\n")

def menu():
    while True:
        print("===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    menu()