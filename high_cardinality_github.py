import pandas as pd

class HighCardinalityHandler:
    def __init__(self, df, threshold=10):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df
        self.threshold = threshold

    def detect_high_cardinality_columns(self):
        """Detect categorical columns with unique values above threshold"""
        self.high_card_cols = [
            col for col in self.df.select_dtypes(include="object").columns
            if self.df[col].nunique() > self.threshold
        ]
        return self.high_card_cols

    def drop_high_cardinality(self):
        """Drop high cardinality columns to reduce noise"""
        self.df_cleaned = self.df.drop(columns=self.high_card_cols)
        return self.df_cleaned

def main():
    data = {
        "UserID": [f"user_{i}" for i in range(30)],
        "Country": ["USA", "FR", "TR", "USA", "DE", "IT"] * 5,
        "Gender": ["F", "M"] * 15,
        "Age": list(range(30))
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df.head())

    app = HighCardinalityHandler(df, threshold=10)
    print("\nHigh cardinality columns:")
    print(app.detect_high_cardinality_columns())

    df_cleaned = app.drop_high_cardinality()
    print("\nCleaned DataFrame:")
    print(df_cleaned.head())

if __name__ == "__main__":
    main()
