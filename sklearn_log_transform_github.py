import pandas as pd
import numpy as np
from sklearn.preprocessing import FunctionTransformer

class CustomFeatureEngineer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df.copy()

    # Log transformation helps normalize highly skewed data by compressing large values 
    # and expanding small ones, improving model performance.
    @staticmethod
    def log_transform(X):
        return np.log1p(X)

    def apply_log_transformation(self, columns):
        transformer = FunctionTransformer(self.log_transform)
        self.df[columns] = transformer.transform(self.df[columns])
        return self.df

def main():
    data = {
        "Income": [1000, 2500, 4000, 10000],
        "Expenses": [500, 800, 2000, 5000]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    engineer = CustomFeatureEngineer(df)
    transformed_df = engineer.apply_log_transformation(["Income", "Expenses"])
    
    print("\nLog-Transformed DataFrame:\n", transformed_df)

if __name__ == "__main__":
    main()
