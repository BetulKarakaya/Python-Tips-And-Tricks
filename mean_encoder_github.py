import pandas as pd
import numpy as np

class TargetMeanEncoder:
    def __init__(self, df, cat_col, target_col):
        self.df = df.copy()
        self.cat_col = cat_col
        self.target_col = target_col

    def encode(self):
        # Calculate mean of target per category
        mean_encoded = self.df.groupby(self.cat_col)[self.target_col].mean()
        # Map the mean value to each category
        self.df[self.cat_col + '_target_mean'] = self.df[self.cat_col].map(mean_encoded)
        return self.df

def main():
    np.random.seed(42)
    df = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'Target': np.random.randint(0, 2, 100)
    })

    print("🔹 Original Data:")
    print(df.head())

    encoder = TargetMeanEncoder(df, 'Category', 'Target')
    encoded_df = encoder.encode()

    print("\n🔸 Target Mean Encoded:")
    print(encoded_df.head())

if __name__ == "__main__":
    main()
