import os

FILE_NAME = "salary.txt"

HRA_RATE = 0.20
DA_RATE = 0.10
PF_RATE = 0.12
TAX_RATE = 0.10
TAX_THRESHOLD = 50000

def load_records():
    records = []
    if not os.path.exists(FILE_NAME):
        return records

    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            emp_id, name, basic, gross, deductions, net = line.split(",")
            records.append({
                "emp_id": emp_id,
                "name": name,
                "basic": float(basic),
                "gross": float(gross),
                "deductions": float(deductions),
                "net": float(net)
            })
    return records

def save_records(records):
    with open(FILE_NAME, "w") as f:
        for r in records:
            f.write(f"{r['emp_id']},{r['name']},{r['basic']:.2f},{r['gross']:.2f},"
                     f"{r['deductions']:.2f},{r['net']:.2f}\n")

def calculate_salary(basic, allowances):
    hra = basic * HRA_RATE
    da = basic * DA_RATE
    gross = basic + hra + da + allowances

    pf = basic * PF_RATE
    tax = gross * TAX_RATE if gross > TAX_THRESHOLD else 0
    deductions = pf + tax

    net = gross - deductions
    return hra, da, gross, pf, tax, deductions, net

def add_salary_record():
    records = load_records()

    emp_id = input("Enter Employee ID: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            print("A salary record for this employee already exists! Use update instead.\n")
            return

    name = input("Enter Employee Name: ").strip()

    try:
        basic = float(input("Enter Basic Pay: ").strip())
        allowances = float(input("Enter Other Allowances (0 if none): ").strip())
    except ValueError:
        print("Invalid number entered. Please try again.\n")
        return

    hra, da, gross, pf, tax, deductions, net = calculate_salary(basic, allowances)

    print("\n----- Salary Breakdown -----")
    print(f"Basic Pay     : {basic:.2f}")
    print(f"HRA (20%)     : {hra:.2f}")
    print(f"DA (10%)      : {da:.2f}")
    print(f"Allowances    : {allowances:.2f}")
    print(f"Gross Salary  : {gross:.2f}")
    print(f"PF (12%)      : {pf:.2f}")
    print(f"Tax           : {tax:.2f}")
    print(f"Total Deduct. : {deductions:.2f}")
    print(f"NET SALARY    : {net:.2f}")
    print("-----------------------------\n")

    records.append({
        "emp_id": emp_id,
        "name": name,
        "basic": basic,
        "gross": gross,
        "deductions": deductions,
        "net": net
    })

    save_records(records)
    print("Salary record saved successfully!\n")

def view_salaries():
    records = load_records()

    if not records:
        print("No salary records found.\n")
        return

    print("\n" + "-" * 80)
    print(f"{'Emp ID':<10}{'Name':<20}{'Basic':<12}{'Gross':<12}{'Deductions':<14}{'Net':<12}")
    print("-" * 80)
    for r in records:
        print(f"{r['emp_id']:<10}{r['name']:<20}{r['basic']:<12.2f}{r['gross']:<12.2f}"
              f"{r['deductions']:<14.2f}{r['net']:<12.2f}")
    print("-" * 80 + "\n")

def search_salary():
    records = load_records()
    emp_id = input("Enter Employee ID to search: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            print("\nSalary Record Found:")
            print(f"Emp ID     : {r['emp_id']}")
            print(f"Name       : {r['name']}")
            print(f"Basic Pay  : {r['basic']:.2f}")
            print(f"Gross      : {r['gross']:.2f}")
            print(f"Deductions : {r['deductions']:.2f}")
            print(f"Net Salary : {r['net']:.2f}\n")
            return

    print("No salary record found for that Employee ID.\n")

def update_salary():
    records = load_records()
    emp_id = input("Enter Employee ID to update: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            try:
                basic = float(input(f"Enter new Basic Pay [{r['basic']:.2f}]: ").strip())
                allowances = float(input("Enter new Other Allowances: ").strip())
            except ValueError:
                print("Invalid number entered. Update cancelled.\n")
                return

            hra, da, gross, pf, tax, deductions, net = calculate_salary(basic, allowances)

            r["basic"] = basic
            r["gross"] = gross
            r["deductions"] = deductions
            r["net"] = net

            save_records(records)
            print("Salary record updated successfully!\n")
            return

    print("No salary record found for that Employee ID.\n")

def delete_salary():
    records = load_records()
    emp_id = input("Enter Employee ID to delete: ").strip()

    for r in records:
        if r["emp_id"] == emp_id:
            confirm = input(f"Delete salary record of {r['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                records.remove(r)
                save_records(records)
                print("Salary record deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    print("No salary record found for that Employee ID.\n")

def menu():
    while True:
        print("===== SALARY MANAGEMENT SYSTEM =====")
        print("1. Add Salary Record")
        print("2. View All Salary Records")
        print("3. Search Salary Record")
        print("4. Update Salary Record")
        print("5. Delete Salary Record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_salary_record()
        elif choice == "2":
            view_salaries()
        elif choice == "3":
            search_salary()
        elif choice == "4":
            update_salary()
        elif choice == "5":
            delete_salary()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    menu()