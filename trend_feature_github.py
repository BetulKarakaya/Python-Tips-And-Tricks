import pandas as pd
import numpy as np

class TrendFeatureEngineer:
    def __init__(self, x_col, y_col, degree=1):
        self.x_col = x_col
        self.y_col = y_col
        self.degree = degree

    def add_trend_feature(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        if self.x_col not in df.columns or self.y_col not in df.columns:
            raise ValueError("❌ Specified columns must exist in the DataFrame.")

        coeffs = np.polyfit(df[self.x_col], df[self.y_col], self.degree)
        poly_func = np.poly1d(coeffs)
        df["trend_feature"] = poly_func(df[self.x_col])

        return df

def main():
    df = pd.DataFrame({
        "Day": np.arange(1, 11),
        "Sales": [100, 120, 150, 170, 200, 220, 250, 280, 300, 330]
    })

    print("Original DataFrame:\n", df)

    trend_engineer = TrendFeatureEngineer(x_col="Day", y_col="Sales", degree=1)
    df_with_trend = trend_engineer.add_trend_feature(df)

    print("\nDataFrame with Trend Feature:\n", df_with_trend)

if __name__ == "__main__":
    main()
