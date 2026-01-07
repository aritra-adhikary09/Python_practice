class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.set_account_holder_name(account_holder_name)
        self.set_account_number(account_number)
        self.set_balance(balance)

    # ---------- Getters ----------
    def get_account_holder_name(self):
        return self.__account_holder_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    # ---------- Setters ----------
    def set_account_holder_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Account holder name must be a string.")
        if name.strip() == "":
            raise ValueError("Account holder name cannot be empty.")
        if len(name.strip()) < 3:
            raise ValueError("Account holder name must be at least 3 characters.")
        self.__account_holder_name = name.strip()

    def set_account_number(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if account_number < 0:
            raise ValueError("Account number cannot be negative.")
        if len(str(account_number)) != 10:
            raise ValueError("Account number must be exactly 10 digits.")
        self.__account_number = account_number

    def set_balance(self, balance):
        if not isinstance(balance, (int, float)):
            raise ValueError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        if balance < 1000:
            raise ValueError("Initial balance must be at least 1000.")
        self.__balance = balance


# ---------- Testing ----------
try:
    acc1 = BankAccount("Aritra Adhikary", 5373112795, 6000)
    print(acc1.get_account_number())
    acc1.set_account_number(123456789)   # invalid
except ValueError as e:
    print(e)

try:
    acc1.set_account_holder_name(45667)  # invalid
except ValueError as e:
    print(e)

try:
    acc1.set_balance(-1)                 # invalid
except ValueError as e:
    print(e)
