employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employees.append([emp_id, name, department, salary])
    print("Employee added successfully.")

def display_employees():
    if not employees:
        print("No employee records found.")
        return
    print(f"{'ID':<8}{'Name':<20}{'Department':<15}{'Salary':<10}")
    for e in employees:
        print(f"{e[0]:<8}{e[1]:<20}{e[2]:<15}{e[3]:<10}")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    for e in employees:
        if e[0] == emp_id:
            print(f"Found: ID: {e[0]}, Name: {e[1]}, Department: {e[2]}, Salary: {e[3]}")
            return
    print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    for e in employees:
        if e[0] == emp_id:
            e[1] = input("Enter new Name: ")
            e[2] = input("Enter new Department: ")
            e[3] = float(input("Enter new Salary: "))
            print("Record updated.")
            return
    print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    for e in employees:
        if e[0] == emp_id:
            employees.remove(e)
            print("Record deleted.")
            return
    print("Employee not found.")

def total_salary():
    if not employees:
        print("No employee records found.")
        return
    total = sum(e[3] for e in employees)
    print(f"Total Salary Expense: {total}")

def menu():
    while True:
        print("\n--- Mini Employee Management System ---")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Total Salary Expense")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            total_salary()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

menu()