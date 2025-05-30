import pandas as pd
import numpy as np
from scipy.stats import zscore

class ZScoreOutlierHandler:
    def __init__(self, df, columns, threshold=3):
        self.df = df.copy()
        self.columns = columns
        self.threshold = threshold

    def handle_outliers(self):
        for col in self.columns:
            z_scores = zscore(self.df[col])
        
            median = self.df[col].median()
            outlier_mask = np.abs(z_scores) > self.threshold
            self.df.loc[outlier_mask, col] = median

        return self.df

def main():
 
    np.random.seed(42)
    data = {
        'Height': np.append(np.random.normal(170, 10, 95), [220, 225, 230, 240, 260]),
        'Weight': np.append(np.random.normal(70, 8, 95), [130, 140, 150, 160, 180])
    }
    df = pd.DataFrame(data)
    print("🔹 Original Data with Outliers:")
    print(df.tail())

    handler = ZScoreOutlierHandler(df, columns=['Height', 'Weight'], threshold=2.5)
    clean_df = handler.handle_outliers()

    print("\n🔸 Cleaned Data:")
    print(clean_df.tail())

if __name__ == "__main__":
    main()
