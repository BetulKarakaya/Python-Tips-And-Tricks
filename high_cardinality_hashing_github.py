import pandas as pd
import numpy as np
from sklearn.feature_extraction import FeatureHasher

class HighCardinalityHandler:
    def __init__(self, df, threshold=10):
        self.df = df.copy()
        self.threshold = threshold
        self.high_card_cols = self._detect_high_card_cols()

    def _detect_high_card_cols(self):
        #Find categorical columns with unique values more than the threshold
        return [col for col in self.df.select_dtypes(include='object').columns 
                if self.df[col].nunique() > self.threshold]

    def apply_frequency_encoding(self):
        for col in self.high_card_cols:
            freq = self.df[col].value_counts()
            self.df[col + "_freq"] = self.df[col].map(freq)
        return self.df

    def apply_hashing(self, n_features=8):
        hasher = FeatureHasher(n_features=n_features, input_type='string')
        for col in self.high_card_cols:
            #convert each value to a list of string (iterable of iterables)
            hashed = hasher.transform([[val] for val in self.df[col].astype(str)])
            hashed_df = pd.DataFrame(hashed.toarray(), 
                                    columns=[f"{col}_hash_{i}" for i in range(n_features)])
            self.df = pd.concat([self.df, hashed_df], axis=1)
            self.df.drop(columns=col, inplace=True)
        return self.df

def main():
    data = {
        'City': np.random.choice([f"City_{i}" for i in range(1, 51)], 100),
        'Occupation': np.random.choice(['Engineer', 'Doctor', 'Artist', 'Lawyer'], 100),
        'Salary': np.random.randint(3000, 9000, 100)
    }
    df = pd.DataFrame(data)
    print("🔹 Original Data:")
    print(df.head())

    print("\n🔸 Frequency Encoding Applied:")
    handler = HighCardinalityHandler(df, threshold=10)
    freq_encoded_df = handler.apply_frequency_encoding()
    print(freq_encoded_df.head())

    print("\n🔸 Hashing Encoding Applied:")
    hashed_df = handler.apply_hashing(n_features=4)
    print(hashed_df.head())

if __name__ == "__main__":
    main()
