import pandas as pd
import numpy as np
from sklearn.feature_selection import mutual_info_classif

class MutualInfoFeatureSelector:
    def __init__(self, df, target, top_n=5):
        self.df = df.copy()
        self.target = target
        self.top_n = top_n

    def select(self):
        X = self.df.drop(columns=self.target)
        y = self.df[self.target]

        #One-hot encode categorical features
        X_encoded = pd.get_dummies(X, drop_first=True)

        #Compute mutual information scores
        mi_scores = mutual_info_classif(X_encoded, y, discrete_features='auto')

        #Store and sort MI scores
        mi_df = pd.DataFrame({
            'Feature': X_encoded.columns,
            'MI Score': mi_scores
        }).sort_values(by='MI Score', ascending=False)

        #Show top N informative features
        print("Top Informative Features:")
        print(mi_df.head(self.top_n).to_string(index=False))

        return mi_df.head(self.top_n)['Feature'].tolist()


def main():
    np.random.seed(0)
    df = pd.DataFrame({
        'age': np.random.randint(18, 70, 100),
        'gender': np.random.choice(['Male', 'Female'], 100),
        'income': np.random.randint(2000, 10000, 100),
        'city': np.random.choice(['A', 'B', 'C', 'D'], 100),
        'purchased': np.random.choice([0, 1], 100)  #Target
    })

    selector = MutualInfoFeatureSelector(df, target='purchased', top_n=3)
    top_features = selector.select()

    print(f"\nSelected Features: {top_features}")

if __name__ == "__main__":
    main()
