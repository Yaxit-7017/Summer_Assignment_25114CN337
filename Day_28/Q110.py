class Account:
    def __init__(self, account_id, name, balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return True


class Bank:
    def __init__(self):
        self.accounts = {}
        self.next_id = 1001

    def create_account(self, name, initial_deposit=0):
        account = Account(self.next_id, name, initial_deposit)
        self.accounts[self.next_id] = account
        self.next_id += 1
        return account.account_id

    def close_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            return True
        return False

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            return False
        return self.accounts[account_id].deposit(amount)

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            return False
        return self.accounts[account_id].withdraw(amount)

    def transfer(self, from_id, to_id, amount):
        if from_id not in self.accounts or to_id not in self.accounts:
            return False
        if not self.accounts[from_id].withdraw(amount):
            return False
        self.accounts[to_id].deposit(amount)
        self.accounts[from_id].transactions.append(f"Transferred {amount} to {to_id}")
        self.accounts[to_id].transactions.append(f"Received {amount} from {from_id}")
        return True

    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].balance
        return None

    def get_statement(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].transactions
        return None

    def list_accounts(self):
        return list(self.accounts.values())


def display_account(account):
    print(f"ID: {account.account_id} | Name: {account.name} | Balance: {account.balance}")


def main():
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. Close Account\n3. Deposit\n4. Withdraw\n5. Transfer"
              "\n6. Check Balance\n7. Statement\n8. List Accounts\n9. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            initial = float(input("Initial deposit: "))
            account_id = bank.create_account(name, initial)
            print(f"Account created with ID {account_id}")

        elif choice == "2":
            account_id = int(input("Account ID: "))
            if bank.close_account(account_id):
                print("Account closed")
            else:
                print("Account not found")

        elif choice == "3":
            account_id = int(input("Account ID: "))
            amount = float(input("Amount: "))
            if bank.deposit(account_id, amount):
                print("Deposit successful")
            else:
                print("Deposit failed")

        elif choice == "4":
            account_id = int(input("Account ID: "))
            amount = float(input("Amount: "))
            if bank.withdraw(account_id, amount):
                print("Withdrawal successful")
            else:
                print("Withdrawal failed")

        elif choice == "5":
            from_id = int(input("From Account ID: "))
            to_id = int(input("To Account ID: "))
            amount = float(input("Amount: "))
            if bank.transfer(from_id, to_id, amount):
                print("Transfer successful")
            else:
                print("Transfer failed")

        elif choice == "6":
            account_id = int(input("Account ID: "))
            balance = bank.get_balance(account_id)
            if balance is not None:
                print(f"Balance: {balance}")
            else:
                print("Account not found")

        elif choice == "7":
            account_id = int(input("Account ID: "))
            statement = bank.get_statement(account_id)
            if statement is not None:
                for t in statement:
                    print(t)
            else:
                print("Account not found")

        elif choice == "8":
            for a in bank.list_accounts():
                display_account(a)

        elif choice == "9":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()