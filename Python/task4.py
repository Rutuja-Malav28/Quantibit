# Design a BankAccount class with methods for deposit, withdrawal, and balance inquiry. 
# Input: 
# account = BankAccount() 
# account.deposit(1000) 
# account.withdraw(200) 
# account.get_balance() 
# Output: 
# Balance after deposit: 1000 
# Balance after withdrawal: 800

class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.balance

account = BankAccount()
account.deposit(1000) 
print(f"Balance after deposit: {account.get_balance()}")  

account.withdraw(200)  
print(f"Balance after withdrawal: {account.get_balance()}")  
