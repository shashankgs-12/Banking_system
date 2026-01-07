class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        print(f"Account {self.account_number} for {self.name} created with balance ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account {self.account_number} ({self.name}): Balance = ${self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = {} # Stores account_number: BankAccount object

    def create_account(self, acc_num, name, initial_deposit=0):
        if acc_num not in self.accounts:
            self.accounts[acc_num] = BankAccount(acc_num, name, initial_deposit)
        else:
            print(f"Account number {acc_num} already exists.")

    def get_account(self, acc_num):
        return self.accounts.get(acc_num)

def main():
    bank = Bank()

    # --- Pre-populate with 3 customers ---
    bank.create_account("101", "Alice", 1000)
    bank.create_account("102", "Bob", 500)
    bank.create_account("103", "Charlie", 200)
    print("\n--- Initial Accounts Created ---\n")

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Check Balance")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a number.")
            else:
                print("Account not found.")
        elif choice == '2':
            acc_num = input("Enter account number: ")
            account = bank.get_account(acc_num)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        elif choice == '3':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



