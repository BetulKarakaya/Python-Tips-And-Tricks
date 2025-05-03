import pandas as pd

class SmartCleaner:
    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("❌ Please provide a valid pandas DataFrame.")
        self.df = data.copy()

    def clean_duplicates(self, subset_cols):
        if not all(col in self.df.columns for col in subset_cols):
            raise ValueError("⚠️ One or more columns not found in DataFrame.")
        
        before = len(self.df)
        self.df.drop_duplicates(subset=subset_cols, inplace=True)
        after = len(self.df)
        print(f"🧹 Removed {before - after} duplicate rows based on {subset_cols}.")

    def show(self, n=5):
        print("Sample of cleaned data:")
        print(self.df.head(n))

def main():
    # Sample DataFrame with duplicates
    data = {
        "name": ["Alice", "Bob", "Alice", "David", "Bob"],
        "city": ["NY", "LA", "NY", "Chicago", "LA"],
        "age": [25, 30, 25, 40, 30]
    }

    df = pd.DataFrame(data)
    cleaner = SmartCleaner(df)

    print("Original DataFrame:")
    print(df, "\n")

    cleaner.clean_duplicates(subset_cols=["name", "city"])
    cleaner.show()

if __name__ == "__main__":
    main()
