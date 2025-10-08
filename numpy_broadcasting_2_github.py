import numpy as np

class GymPricing:
    def __init__(self, base_prices: np.ndarray, increase_percentages: np.ndarray, branches: list):
        """
        base_prices: monthly membership prices for different gym branches
        increase_percentages: percentage increases for each month
        branches: list of branch names
        """
        self.base_prices = base_prices
        self.increase_percentages = increase_percentages / 100  # convert to decimal
        self.branches = branches

    def calculate_new_prices(self):
        """Apply monthly increases using broadcasting."""
        return self.base_prices * (1 + self.increase_percentages[:, np.newaxis])

    def display_price_table(self):
        """Show monthly price evolution for each gym branch."""
        updated_prices = self.calculate_new_prices()

        #Header
        header = " | ".join([f"{b:^8}" for b in self.branches])
        print("Gym Membership Price Updates:")
        print("-" * (len(header) + 15))
        print(f"{'Branches':<8} | {header}")
        print("-" * (len(header) + 15))

        #Table
        for i, month_prices in enumerate(updated_prices, start=1):
            prices = " | ".join(f"${p:.2f}" for p in month_prices)
            print(f"{f'Month {i}':<8} | {prices}")

        print("-" * (len(header) + 15))
        print("All prices include monthly increases.\n")

def main():
    #Base prices for gym branches (A, B, C)
    base_prices = np.array([300, 350, 400])  
    branches = ["A", "B", "C"]

    #Monthly increase percentages over 4 months
    increase_percentages = np.array([0, 5, 10, 15])  

    gym = GymPricing(base_prices, increase_percentages, branches)
    gym.display_price_table()

if __name__ == "__main__":
    main()
