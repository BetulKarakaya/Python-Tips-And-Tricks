class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private attribute (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}$ deposited. New balance: {self.__balance}$")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}$ withdrawn. Remaining balance: {self.__balance}$")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance


def main():
    account = BankAccount("Betül", 1000)
    account.deposit(500)
    account.withdraw(200)
    print("Final Balance:", account.get_balance())

    # ATTEMPT to access balance directly from outside
    account.__balance = 999999
    print("After hacking attempt, balance is still:", account.get_balance())


if __name__ == "__main__":
    main()
