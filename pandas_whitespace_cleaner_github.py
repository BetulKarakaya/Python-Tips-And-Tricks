import pandas as pd

class WhitespaceCleaner:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df

    def clean_whitespace(self):
        str_cols = self.df.select_dtypes(include='object').columns
        self.df[str_cols] = self.df[str_cols].apply(lambda x: x.str.strip())
        return self.df

def main():
    data = {
        "Name": ["Betül ", "   Mert", "Zeynep", "Ali "],
        "City": [" Ankara", "İstanbul ", " İzmir ", "Bursa"],
        "Age": [25, 30, 27, 22]
    }

    df = pd.DataFrame(data)
    print("Before Cleaning:\n", df)

    cleaner = WhitespaceCleaner(df)
    cleaned_df = cleaner.clean_whitespace()

    print("\nAfter Cleaning:\n", cleaned_df)

if __name__ == "__main__":
    main()
