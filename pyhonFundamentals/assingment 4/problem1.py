'''Create a BankAccount class with attributes account_number, owner_name, and balance.

Add methods to deposit, withdraw, and check balance.**'''

class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.accountNo= account_number
        self.ownerName= owner_name
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount}Rs has been debited into {self.accountNo}.remaining balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("You have insufficient balance.")
        else: # balance is either same or more than amount user wants to deduct
            self.balance -= amount
            print(f"{self.balance}RS has been withdrawn from account number: {self.accountNo}")
    
    def check_balance(self):
        print(f"{self.balance}RS has in this account no- {self.accountNo}")

    
acc1 = BankAccount(5373112795,"Aritra Adhikary",70000)

acc1.check_balance()
