import pandas as pd
import numpy as np

class TargetEncoder:
    def __init__(self, df, target, smoothing=10):
        self.df = df.copy()
        self.target = target
        self.smoothing = smoothing

    def encode(self, column):
        means = self.df.groupby(column)[self.target].mean()
        counts = self.df.groupby(column)[self.target].count()
        global_mean = self.df[self.target].mean()

        # Smoothing formula
        smooth = (means * counts + global_mean * self.smoothing) / (counts + self.smoothing)

        # Map back to dataframe
        new_col_name = f"{column}_target_enc"
        self.df[new_col_name] = self.df[column].map(smooth)
        return self.df[[column, new_col_name]].drop_duplicates().head()

def main():
    np.random.seed(1)
    df = pd.DataFrame({
        'Category': np.random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 100),
        'Purchased': np.random.randint(0, 2, 100)
    })

    print("🔹 Original Data:")
    print(df.head())

    encoder = TargetEncoder(df, target='Purchased', smoothing=5)
    encoded = encoder.encode('Category')

    print("\n🔸 Target Encoding (with smoothing) result:")
    print(encoded)

if __name__ == "__main__":
    main()
