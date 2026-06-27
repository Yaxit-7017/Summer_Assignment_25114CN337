import os
from datetime import datetime

FILE_NAME = "marksheet.txt"
SUBJECTS = ["Mathematics", "Science", "English", "Computer Science", "Social Studies"]
MAX_MARKS_PER_SUBJECT = 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"

def get_marks():
    marks = {}
    print(f"\nEnter marks out of {MAX_MARKS_PER_SUBJECT} for each subject:")
    for subject in SUBJECTS:
        while True:
            try:
                m = float(input(f"  {subject}: ").strip())
                if 0 <= m <= MAX_MARKS_PER_SUBJECT:
                    marks[subject] = m
                    break
                else:
                    print(f"  Please enter a value between 0 and {MAX_MARKS_PER_SUBJECT}.")
            except ValueError:
                print("  Invalid input. Please enter a number.")
    return marks

def generate_marksheet():
    roll_no = input("Enter Roll Number: ").strip()
    name = input("Enter Student Name: ").strip()
    student_class = input("Enter Class/Course: ").strip()

    marks = get_marks()

    total_obtained = sum(marks.values())
    total_max = MAX_MARKS_PER_SUBJECT * len(SUBJECTS)
    percentage = (total_obtained / total_max) * 100
    grade = calculate_grade(percentage)
    result = "PASS" if percentage >= 40 and all(m >= 33 for m in marks.values()) else "FAIL"

    print_marksheet(roll_no, name, student_class, marks, total_obtained, total_max, percentage, grade, result)

    save_marksheet(roll_no, name, student_class, marks, total_obtained, percentage, grade, result)

    print("Marksheet generated and saved successfully!\n")

def print_marksheet(roll_no, name, student_class, marks, total_obtained, total_max, percentage, grade, result):
    print("\n" + "=" * 50)
    print(f"{'STUDENT MARKSHEET':^50}")
    print("=" * 50)
    print(f"Roll No : {roll_no}")
    print(f"Name    : {name}")
    print(f"Class   : {student_class}")
    print(f"Date    : {datetime.now().strftime('%d-%m-%Y')}")
    print("-" * 50)
    print(f"{'Subject':<25}{'Marks Obtained':<15}{'Max Marks':<10}")
    print("-" * 50)
    for subject, m in marks.items():
        print(f"{subject:<25}{m:<15.1f}{MAX_MARKS_PER_SUBJECT:<10}")
    print("-" * 50)
    print(f"{'Total':<25}{total_obtained:<15.1f}{total_max:<10}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {result}")
    print("=" * 50 + "\n")

def save_marksheet(roll_no, name, student_class, marks, total_obtained, percentage, grade, result):
    with open(FILE_NAME, "a") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Roll No : {roll_no}\n")
        f.write(f"Name    : {name}\n")
        f.write(f"Class   : {student_class}\n")
        f.write(f"Date    : {datetime.now().strftime('%d-%m-%Y')}\n")
        f.write("-" * 50 + "\n")
        for subject, m in marks.items():
            f.write(f"{subject:<25}{m:<10.1f}/ {MAX_MARKS_PER_SUBJECT}\n")
        f.write("-" * 50 + "\n")
        f.write(f"Total Obtained : {total_obtained:.1f}\n")
        f.write(f"Percentage     : {percentage:.2f}%\n")
        f.write(f"Grade          : {grade}\n")
        f.write(f"Result         : {result}\n")
        f.write("=" * 50 + "\n\n")

def view_all_marksheets():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No marksheets have been generated yet.\n")
        return

    with open(FILE_NAME, "r") as f:
        print(f.read())

def search_marksheet():
    if not os.path.exists(FILE_NAME):
        print("No marksheets have been generated yet.\n")
        return

    roll_no = input("Enter Roll Number to search: ").strip()

    with open(FILE_NAME, "r") as f:
        content = f.read()

    blocks = content.strip().split("=" * 50 + "\n\n")
    found = False
    for block in blocks:
        if f"Roll No : {roll_no}" in block:
            print("\n" + "=" * 50)
            print(block.strip())
            print("=" * 50 + "\n")
            found = True

    if not found:
        print("No marksheet found for that roll number.\n")

def menu():
    while True:
        print("===== MARKSHEET GENERATION SYSTEM =====")
        print("1. Generate New Marksheet")
        print("2. View All Marksheets")
        print("3. Search Marksheet by Roll Number")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            generate_marksheet()
        elif choice == "2":
            view_all_marksheets()
        elif choice == "3":
            search_marksheet()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    menu()