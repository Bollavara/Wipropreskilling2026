class BankAccount:
    def __init__(self, account_number, balance):  # Parameterized constructor
        self.account_number = account_number
        self.balance = balance
        print("Account created:", self.account_number)

    def deposit(self, amount):  # Deposit method(Parameterized method)
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            print("Current Balance:", self.balance)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):  # Withdraw method(Parameterized method)
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)

    def __del__(self):  # Destructor
        print("Account deleted:", self.account_number)

account = BankAccount(8765954, 10000)  #Object creation

account.deposit(5000)
account.withdraw(7000)
account.withdraw(7000)   # Invalid withdrawal
