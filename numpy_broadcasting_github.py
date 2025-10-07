import numpy as np

class SalesAnalyzer:
    def __init__(self, daily_sales: np.ndarray, price_per_unit: np.ndarray):
        """
        daily_sales: number of products sold each day (rows = days, columns = products)
        price_per_unit: price per product (1D array)
        """
        self.daily_sales = daily_sales
        self.price_per_unit = price_per_unit

    def total_revenue_per_day(self):
        """Use broadcasting to calculate daily revenue."""
        return np.sum(self.daily_sales * self.price_per_unit, axis=1)

    def display_report(self):
        """Show a formatted revenue report."""
        print("### Daily Sales Report:")
        print("-" * 40)
        for i, revenue in enumerate(self.total_revenue_per_day(), start=1):
            print(f"Day {i}: ${revenue}")
        print("-" * 40)
        print(f"Total Revenue: ${np.sum(self.total_revenue_per_day())}")

def main():
    #Each row = [apples, milk, bread] sold per day
    daily_sales = np.array([
        [10, 5, 8],
        [7, 6, 9],
        [12, 4, 6]
    ])

    #Price per unit for each product → apples, milk, bread
    price_per_unit = np.array([2, 5, 3])

    analyzer = SalesAnalyzer(daily_sales, price_per_unit)
    analyzer.display_report()

if __name__ == "__main__":
    main()
