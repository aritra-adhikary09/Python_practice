from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"{amount} Rs has been credited from your credit card."


class UPIPayment(Payment):
    def process_payment(self, amount):
        return f"{amount} Rs has been credited via UPI."


class CashPayment(Payment):
    def process_payment(self, amount):
        return f"{amount} Rs has been received in cash."


payments = [
    CreditCardPayment(),
    UPIPayment(),
    CashPayment()
]

amounts = [12000, 10000, 8000]

for payment, amount in zip(payments, amounts):
    print(payment.process_payment(amount))

