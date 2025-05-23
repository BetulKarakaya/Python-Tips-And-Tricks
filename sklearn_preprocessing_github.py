from sklearn.preprocessing import FunctionTransformer
import numpy as np
import pandas as pd

class LogTransformer:
    def __init__(self, col_name):
        self.col_name = col_name
        self.transformer = FunctionTransformer(self._log_transform, validate=False)

    def _log_transform(self, X):
        X = X.copy()
        X[self.col_name] = np.log1p(X[self.col_name])
        return X

    def transform(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        return self.transformer.transform(df)

def main():
    df = pd.DataFrame({
        "Salary": [50000, 60000, 75000, 120000],
        "Experience": [1, 3, 5, 7]
    })
    
    print("Original DataFrame:\n", df)

    transformer = LogTransformer(col_name="Salary")
    df_transformed = transformer.transform(df)

    print("\nTransformed DataFrame:\n", df_transformed)

if __name__ == "__main__":
    main()
