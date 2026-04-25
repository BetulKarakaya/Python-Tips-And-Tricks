import numpy as np
import pandas as pd

class TrendAnalyzer:
    """
    A class to perform lightning-fast rolling window 
    analytics using NumPy stride tricks.
    """
    def __init__(self, data):
        self.data = np.array(data)

    def __str__(self):
        return f"Trend Analyzer ready for {len(self.data)} data points."

    def get_rolling_stats(self, window_size=7):
        """
        TRICK: sliding_window_view()
        Instead of duplicating data, it creates a 'view' that 
        re-indexes the existing memory into windows.
        """
        # Create a view of shape (N - window_size + 1, window_size)
        windows = np.lib.stride_tricks.sliding_window_view(self.data, window_size)
        
        # Now we can perform ANY vectorized operation across the windows
        rolling_mean = np.mean(windows, axis=1)
        rolling_std = np.std(windows, axis=1)
        
        return rolling_mean, rolling_std

def main():
    # 1. Simulate 1 year of daily student study hours (365 days)
    np.random.seed(42)
    daily_hours = np.random.normal(6, 2, 365)

    # 2. Initialize Analyzer
    analyzer = TrendAnalyzer(daily_hours)
    
    # 3. Calculate 7-day moving average and volatility
    means, stds = analyzer.get_rolling_stats(window_size=7)

    # 4. Display Results
    print(f"--- Trend Analysis (First 10 Windows) ---")
    results = pd.DataFrame({
        "Rolling_Mean": means[:10],
        "Rolling_Volatility": stds[:10]
    })
    print(results.round(2))

if __name__ == "__main__":
    main()