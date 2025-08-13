from abc import ABC, abstractmethod

# ---------------- Abstract Base Class ---------------- #
class BankAccount(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def show_balance(self):
        """Display the current balance."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from the account."""
        pass

# ---------------- Concrete Classes ---------------- #
class CheckingAccount(BankAccount):
    def show_balance(self):
        print(f"[Checking] {self.owner}'s balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from Checking. New balance: ${self.balance}")
        else:
            print("❌ Not enough funds in Checking.")

class SavingsAccount(BankAccount):
    def show_balance(self):
        print(f"[Savings] {self.owner}'s balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from Savings. New balance: ${self.balance}")
        else:
            print("❌ Not enough funds in Savings.")

def main():
    john_checking = CheckingAccount("John", 1000)
    john_savings = SavingsAccount("John", 5000)

    john_checking.show_balance()
    john_checking.withdraw(200)

    john_savings.show_balance()
    john_savings.withdraw(6000)  # Should show not enough funds

if __name__ == "__main__":
    main()
