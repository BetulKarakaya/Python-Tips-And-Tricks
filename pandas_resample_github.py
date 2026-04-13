import pandas as pd
import numpy as np

class TimeSeriesAnalyzer:
    """
    A class to handle time-series data and perform 
    frequency-based aggregations efficiently.
    """
    def __init__(self, data):
        # Time-series operations require a DatetimeIndex
        self.df = pd.DataFrame(data)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.set_index('Date')

    def __str__(self):
        return f"Dataset spans from {self.df.index.min()} to {self.df.index.max()}"

    def get_weekly_summary(self):
        """
        TRICK: Resampling.
        'W' stands for Weekly. We can use 'M' for Monthly or 'D' for Daily.
        This calculates the total and average sales for each week.
        """
        summary = self.df['Sales'].resample('W').agg(['sum', 'mean'])
        return summary

def main():
    # 1. Generating 30 days of random sales data
    data = {
        'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
        'Sales': np.random.randint(100, 500, 30)
    }

    # 2. Initialize Analyzer
    analyzer = TimeSeriesAnalyzer(data=data)
    print(analyzer)

    # 3. Execute Weekly Resample
    weekly_report = analyzer.get_weekly_summary()

    # Display Results
    print("\n--- Weekly Sales Summary ---")
    print(weekly_report)

if __name__ == "__main__":
    main()