from abc import ABC, abstractmethod

class PaymentMethod(ABC):  # Abstract Base Class
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount}$ using Credit Card {self.card_number[-4:]}.")

    def refund(self, amount):
        print(f"Refunded {amount}$ back to Credit Card {self.card_number[-4:]}.")


class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount}$ using PayPal account {self.email}.")

    def refund(self, amount):
        print(f"Refunded {amount}$ back to PayPal account {self.email}.")


def main():
    payments = [
        CreditCardPayment("1234567812345678"),
        PayPalPayment("user@example.com")
    ]

    for p in payments:
        p.pay(100)
        p.refund(50)


if __name__ == "__main__":
    main()
