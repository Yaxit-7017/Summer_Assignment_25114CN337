class ATM:
    def __init__(self, balance=1000.0, pin="1234"):
        self.balance = balance
        self.pin = pin
        self.authenticated = False

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ").strip()
            if entered_pin == self.pin:
                self.authenticated = True
                print("Authentication successful!\n")
                return True
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
        print("Too many incorrect attempts. Card locked.")
        return False

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
        except ValueError:
            print("Invalid amount.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")
        self.check_balance()

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
        except ValueError:
            print("Invalid amount.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        if amount % 100 != 0:
            print("Please enter an amount in multiples of 100.")
            return
        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
        self.check_balance()

    def change_pin(self):
        old_pin = input("Enter current PIN: ").strip()
        if old_pin != self.pin:
            print("Incorrect current PIN.")
            return
        new_pin = input("Enter new 4-digit PIN: ").strip()
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be exactly 4 digits.")
            return
        self.pin = new_pin
        print("PIN changed successfully.")

    def run(self):
        print("=== Welcome to the ATM ===")
        if not self.authenticate():
            return

        while True:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1-5.")

if __name__ == "__main__":
    atm = ATM(balance=5000.0, pin="1234")
    atm.run()