'''Create a BankAccount class with attributes account_number, owner_name, and balance.

Add methods to deposit, withdraw, and check balance.**'''

class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.AcNo = account_number
        self.OwnName = owner_name
        self.balance = balance
    
    def deposit(self,deposit):
        self.balance+= deposit
        print(f"{deposit}Rs has been deposited into your bankaccount.")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insuffcient balance on your bankaccount.")
        else:
            self.balance-=amount
            print(f"{amount}Rs has been credited from your bankaccont.")
    def Balance(self):
        print(f"{self.balance}Rs in your bankaccount.")

acc1 = BankAccount(123414,"Aritra Adhikary",40_000)

acc1.deposit(3000)