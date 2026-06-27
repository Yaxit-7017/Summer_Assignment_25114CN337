import os

FILE_NAME = "employees.txt"

def load_records():
    records = []
    if not os.path.exists(FILE_NAME):
        return records

    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            emp_id, name, department, designation, phone = line.split(",")
            records.append({
                "emp_id": emp_id,
                "name": name,
                "department": department,
                "designation": designation,
                "phone": phone
            })
    return records

def save_records(records):
    with open(FILE_NAME, "w") as f:
        for r in records:
            f.write(f"{r['emp_id']},{r['name']},{r['department']},{r['designation']},{r['phone']}\n")

def add_employee():
    records = load_records()

    emp_id = input("Enter Employee ID: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            print("An employee with this ID already exists!\n")
            return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    designation = input("Enter Designation: ").strip()
    phone = input("Enter Phone Number: ").strip()

    records.append({
        "emp_id": emp_id,
        "name": name,
        "department": department,
        "designation": designation,
        "phone": phone
    })

    save_records(records)
    print("Employee record added successfully!\n")

def view_employees():
    records = load_records()

    if not records:
        print("No employee records found.\n")
        return

    print("\n" + "-" * 85)
    print(f"{'Emp ID':<10}{'Name':<20}{'Department':<18}{'Designation':<18}{'Phone':<12}")
    print("-" * 85)
    for r in records:
        print(f"{r['emp_id']:<10}{r['name']:<20}{r['department']:<18}{r['designation']:<18}{r['phone']:<12}")
    print("-" * 85 + "\n")

def search_employee():
    records = load_records()
    emp_id = input("Enter Employee ID to search: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            print("\nEmployee Found:")
            print(f"Emp ID      : {r['emp_id']}")
            print(f"Name        : {r['name']}")
            print(f"Department  : {r['department']}")
            print(f"Designation : {r['designation']}")
            print(f"Phone       : {r['phone']}\n")
            return

    print("No employee found with that ID.\n")

def update_employee():
    records = load_records()
    emp_id = input("Enter Employee ID to update: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            print("Leave a field blank to keep its current value.")

            name = input(f"Name [{r['name']}]: ").strip()
            department = input(f"Department [{r['department']}]: ").strip()
            designation = input(f"Designation [{r['designation']}]: ").strip()
            phone = input(f"Phone [{r['phone']}]: ").strip()

            if name:
                r["name"] = name
            if department:
                r["department"] = department
            if designation:
                r["designation"] = designation
            if phone:
                r["phone"] = phone

            save_records(records)
            print("Employee record updated successfully!\n")
            return

    print("No employee found with that ID.\n")

def delete_employee():
    records = load_records()
    emp_id = input("Enter Employee ID to delete: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            confirm = input(f"Delete record of {r['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                records.remove(r)
                save_records(records)
                print("Employee record deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    print("No employee found with that ID.\n")

def menu():
    while True:
        print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    menu()