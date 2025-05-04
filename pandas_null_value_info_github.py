import pandas as pd

class MissingDataAnalyzer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df

    def analyze(self):
        print("Analyzing missing data...\n")
        missing_summary = self.df.isnull().sum()
        total_missing = missing_summary.sum()

        if total_missing == 0:
            print("No missing values found!")
        else:
            print("Missing values per column:")
            for col, count in missing_summary.items():
                if count > 0:
                    print(f"🔹 {col}: {count}")

def main():
    data = {
        "Name": ["Alice", "Bob", None, "David"],
        "Age": [25, None, 30, 22],
        "City": ["NY", "LA", "Chicago", None]
    }

    df = pd.DataFrame(data)
    analyzer = MissingDataAnalyzer(df)
    analyzer.analyze()

if __name__ == "__main__":
    main()
