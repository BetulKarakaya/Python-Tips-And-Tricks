from collections import defaultdict
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # { '2025-06-18': { 'Grocery': 150.75, 'Entertainment': 80 } }
        self.expenses = defaultdict(lambda: defaultdict(float))

    def add_expense(self, category, amount, date_str=None):
        if amount < 0:
            print("Amount cannot be negative!")
            return
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        self.expenses[date_str][category] += amount
        print(f"-Added {amount} TL to {category} on {date_str}.")

    def report_by_date(self, date_str):
        if date_str not in self.expenses:
            print(f"-No expenses found for {date_str}.")
            return
        print(f"\n-Expenses on {date_str}:")
        for category, total in self.expenses[date_str].items():
            print(f" - {category}: {total} TL")

    def report_all(self):
        print("\n-All expenses:")
        for date_str, categories in self.expenses.items():
            print(f"Date: {date_str}")
            for category, total in categories.items():
                print(f"  - {category}: {total} TL")
            print("")


def main():
    tracker = ExpenseTracker()

    tracker.add_expense("Grocery", 150.75)
    tracker.add_expense("Entertainment", 80, "2025-06-15")
    tracker.add_expense("Grocery", 50.25, "2025-06-15")

    tracker.report_by_date("2025-06-15")
    tracker.report_all()

if __name__ == "__main__":
    main()