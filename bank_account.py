class BankAccount:
    account_holder = str
    balance = float = 0.0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance+amount
        print(f"Current Account balance is {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
            print(f"After Withdrawing your current Account balance is {self.balance}")
        else:
            print(f"Account balance is not sufficient. Current balance is {self.balance}")
    
    def display_balance(self):
        print(f"Your current account balance is {self.balance}")

    
user1 = BankAccount('alex', 0)
user1.deposit(1000)
user1.withdraw(1000)
