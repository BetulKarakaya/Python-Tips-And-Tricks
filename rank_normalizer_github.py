import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import QuantileTransformer

class RankNormalizer:
    def __init__(self, df):
        self.df = df.copy()

    def apply_rank_norm(self, cols):
        # Apply rank-based normalization
        qt = QuantileTransformer(output_distribution='normal', random_state=42)
        self.df[cols] = qt.fit_transform(self.df[cols])
        return self.df

def main():
    np.random.seed(42)
    df = pd.DataFrame({
        'income': np.random.exponential(scale=5000, size=100),
        'expenses': np.random.exponential(scale=3000, size=100)
    })

    print("Before Rank Normalization:")
    print(df.head())

    # Plot original income distribution
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df['income'], kde=True, bins=30, color='salmon')
    plt.title("Original 'income' Distribution")

    # Apply normalization
    normalizer = RankNormalizer(df)
    normalized_df = normalizer.apply_rank_norm(['income', 'expenses'])

    print("\nAfter Rank Normalization:")
    print(normalized_df.head())

    # Plot normalized income distribution
    plt.subplot(1, 2, 2)
    sns.histplot(normalized_df['income'], kde=True, bins=30, color='skyblue')
    plt.title("Normalized 'income' Distribution (Gaussian)")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
