from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

# PolynomialFeatures expands the feature space by generating polynomial and 
# interaction terms, enabling linear models to capture non-linear relationships.

class FeatureInteractionGenerator:
    def __init__(self, degree=2, interaction_only=True):
        self.poly = PolynomialFeatures(degree=degree, interaction_only=interaction_only, include_bias=False)

    def generate(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        
        try:
            transformed = self.poly.fit_transform(df)
            feature_names = self.poly.get_feature_names_out(df.columns)
            return pd.DataFrame(transformed, columns=feature_names)
        except Exception as e:
            raise ValueError(f"⚠️ Failed to generate interactions: {e}")

def main():
    data = {
        "Temperature": [25, 30, 35],
        "Humidity": [60, 55, 50],
        "WindSpeed": [10, 15, 12]
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)

    print("\nInteraction Features (2nd degree):")
    generator = FeatureInteractionGenerator()
    df_interactions = generator.generate(df)
    print(df_interactions)

if __name__ == "__main__":
    main()
