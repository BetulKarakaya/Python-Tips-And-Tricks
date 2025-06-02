import pandas as pd
import numpy as np

class OutlierCapping:
    def __init__(self, df, columns):
        self.df = df.copy()
        self.columns = columns

    def cap_outliers(self):
        for col in self.columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            # Winsorize: Cap values at the thresholds
            self.df[col] = np.where(self.df[col] < lower, lower, self.df[col])
            self.df[col] = np.where(self.df[col] > upper, upper, self.df[col])
        return self.df

def main():
    np.random.seed(42)
    df = pd.DataFrame({
        'Income': np.random.normal(5000, 1500, 100).tolist() + [15000, 16000, 17000],
        'Age': np.random.normal(35, 10, 100).tolist() + [80, 85, 90]
    })

    print("🔹 Before Capping:")
    print(df.describe())

    capper = OutlierCapping(df, columns=['Income', 'Age'])
    capped_df = capper.cap_outliers()

    print("\n🔸 After Capping:")
    print(capped_df.describe())

if __name__ == "__main__":
    main()
