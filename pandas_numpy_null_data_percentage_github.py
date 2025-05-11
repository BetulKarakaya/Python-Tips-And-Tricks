import pandas as pd
import numpy as np

class MissingDataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ The input must be a pandas DataFrame.")
        self.df = df.copy()

    def analyze(self):
        print("Let's explore the missing data situation column by column:\n")
        for column in self.df.columns:
            total = self.df[column].isnull().sum()
            percentage = (total / len(self.df)) * 100

            if total == 0:
                status = "🟢 No missing data"
            elif percentage < 10:
                status = "🟡 Mild missing data"
            elif percentage < 50:
                status = "🟠 Moderate missing data"
            else:
                status = "🔴 Severe missing data"

            print(f"{column}: {total} missing ({percentage:.2f}%) → {status}")

def main():
    #Simulate a DataFrame with various levels of missing data
    data = {
        "Name": ["Betül", "Ali", None, "Mert", None],
        "Age": [25, None, 22, 30, 29],
        "City": ["Ankara", "İstanbul", "İzmir", None, None],
        "Salary": [4000, 5000, None, None, None],
        "Department": ["IT","HR","R&D","Sales","Management"]
    }
    df = pd.DataFrame(data)

    analyzer = MissingDataAnalyzer(df)
    analyzer.analyze()

if __name__ == "__main__":
    main()
