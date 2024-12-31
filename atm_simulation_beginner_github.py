def atm_simulator():
    """
    Simulates an ATM where you can check balance, deposit, and withdraw money.
    Uses built-in functions like input(), sum(), and enumerate() for functionality.
    """
    print("💳 Welcome to the Python ATM! 💳")
    balance = 1000  # Starting balance
    transactions = []  # Keep track of all transactions

    while True:
        print("\n🔸 What would you like to do?")
        print("1. Check Balance 🏦")
        print("2. Deposit Money 💰")
        print("3. Withdraw Money 💸")
        print("4. Transaction History 📜")
        print("5. Exit 🚪")

        # Get the user's choice
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Check balance
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == "2":
            # Deposit money
            amount = float(input("Enter the amount to deposit: $"))
            balance += amount
            transactions.append(("Deposit", amount))
            print(f"${amount:.2f} deposited successfully!")
        elif choice == "3":
            # Withdraw money
            amount = float(input("Enter the amount to withdraw: $"))
            if amount > balance:
                print("❌ Insufficient funds!")
            else:
                balance -= amount
                transactions.append(("Withdrawal", amount))
                print(f"${amount:.2f} withdrawn successfully!")
        elif choice == "4":
            # Show transaction history
            if not transactions:
                print("No transactions yet!")
            else:
                print("\n📜 Transaction History 📜")
                for i, (type_, amount) in enumerate(transactions, start=1):
                    print(f"{i}. {type_}: ${amount:.2f}")
        elif choice == "5":
            # Exit
            print("Thank you for using the Python ATM. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

def main():
    atm_simulator()
if __name__ == "__main__":
    main()
