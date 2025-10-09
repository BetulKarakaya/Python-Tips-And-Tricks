from itertools import tee

class SalesTracker:
    def __init__(self, sales_data):
        """
        sales_data: iterable of daily sales amounts.
        """
        self.sales_data = iter(sales_data)  # converting to iterator

    def analyze_sales(self):
        """Duplicate iterator to perform multiple analyses."""
        sales1, sales2 = tee(self.sales_data, 2)

        total = sum(sales1)
        avg = total / len(list(sales2))  # consume second iterator to get count

        print(f"Total Sales: ${total}")
        print(f"Average Daily Sales: ${avg:.2f}")

def main():
    #Example: daily sales over a week
    weekly_sales = [1200, 1500, 1300, 1100, 1600, 2000, 1750]
    tracker = SalesTracker(weekly_sales)
    tracker.analyze_sales()

if __name__ == "__main__":
    main()
