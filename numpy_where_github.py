import pandas as pd
import numpy as np

class FastLabeling:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df

    @staticmethod
    def label_age_group(df):
        df["Age_Group"] = np.where(df["Age"] > 30, "Adult", "Young")
        return df

def main():
    data = {
        "Name": ["Betül", "Ahmet", "Zeynep", "Ali"],
        "Age": [25, 34, 29, 45]
    }
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    processor = FastLabeling(df)
    updated_df = processor.label_age_group(df)

    print("\nAge Groups Labeled:\n", updated_df)

if __name__ == "__main__":
    main()
