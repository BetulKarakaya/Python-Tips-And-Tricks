import pandas as pd

class PortfolioAnalyzer:
    """
    A class to analyze financial asset performance and volatility.
    """
    def __init__(self, data):
        # We set the Date as the index to handle time-series logic correctly
        self.df = pd.DataFrame(data).set_index('Date')

    def __str__(self):
        return f"Current Portfolio Data:\n{self.df.to_string()}"

    def calculate_daily_returns(self):
        """
        Calculates the percentage change between consecutive rows.
        'fill_value=0' handles the first row which has no previous day.
        """
        return self.df.pct_change(fill_method=None).fillna(0) * 100

    def get_highest_volatility_asset(self):
        """
        Identifies which asset had the largest single-day price swing.
        """
        returns = self.calculate_daily_returns()
        return returns.std().idxmax()

def main():
    # Sample Dataset: Closing prices of different assets over 5 days
    portfolio_data = {
        'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
        'Bitcoin': [42000, 43500, 41000, 44000, 45000],
        'Gold': [2050, 2060, 2055, 2070, 2065],
        'S&P 500': [4700, 4720, 4710, 4750, 4780]
    }

    # Initialize the analyzer
    analyzer = PortfolioAnalyzer(data=portfolio_data)

    # 1. Get Daily Percentage Returns
    daily_changes = analyzer.calculate_daily_returns()

    # 2. Find the most volatile asset
    volatile_asset = analyzer.get_highest_volatility_asset()

    # Display Results
    print("--- Asset Price Evolution ---")
    print(analyzer)
    
    print("\n--- Daily Returns (%) ---")
    print(daily_changes.round(2))
    
    print(f"\nMost Volatile Asset: {volatile_asset}")

if __name__ == "__main__":
    main()