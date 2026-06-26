def check_voting_eligibility():
    print("=== Voting Eligibility System ===")
    name = input("Enter your name: ").strip()

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Invalid age entered.")
        return

    citizen_input = input("Are you a citizen of the country? (yes/no): ").strip().lower()
    is_citizen = citizen_input == "yes"

    registered_input = input("Are you registered to vote? (yes/no): ").strip().lower()
    is_registered = registered_input == "yes"

    print("\n--- Eligibility Result ---")

    if age < 0:
        print("Age cannot be negative.")
        return

    if age < 18:
        print(f"{name}, you are not eligible to vote. Minimum age is 18 (you are {age}).")
        return

    if not is_citizen:
        print(f"{name}, you are not eligible to vote. You must be a citizen.")
        return

    if not is_registered:
        print(f"{name}, you meet age and citizenship requirements, but you must register to vote first.")
        return

    print(f"{name}, you are ELIGIBLE to vote!")

if __name__ == "__main__":
    check_voting_eligibility()