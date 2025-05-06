import pandas as pd
import numpy as np

class AgeAnalyzer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        if "Age" not in df.columns:
            raise ValueError("❌ DataFrame must contain an 'Age' column.")
        self.df = df

    def get_age_array(self):
        return self.df["Age"].to_numpy()

    def calculate_average_age(self):
        age_array = self.get_age_array()
        return np.mean(age_array)
    

def main():
    data = {
        "Name": ["Betül", "Mert", "Zeynep", "Ali"],
        "Age": [25, 30, 27, 22],
        "City": ["Ankara", "İstanbul", "İzmir", "Bursa"]
    }
    df = pd.DataFrame(data)

    app = AgeAnalyzer(df)
    age_array = app.get_age_array()
    print("Age Array:", age_array)

    average_age = app.calculate_average_age()
    print(f"Average Age: {average_age:.1f} years")


if __name__ == "__main__":
    main()
