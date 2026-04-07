import pandas as pd

class FeatureEncoder:
    """
    A class to handle categorical data transformation 
    for machine learning readiness.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Raw Data Structure:\n{self.df.to_string()}"

    def encode_categories(self, columns_to_encode):
        """
        Transfers categorical text into a binary indicator matrix.
        Using 'dtype=int' keeps the output clean (0/1 instead of True/False).
        """
        # TRICK: get_dummies expands one column into multiple binary columns
        self.encoded_df = pd.get_dummies(
            self.df, 
            columns=columns_to_encode, 
            prefix="is", 
            dtype=int
        )
        return self.encoded_df

def main():
    # Sample Dataset: Car inventory with categorical features
    car_inventory = {
        'Car_ID': [1, 2, 3, 4],
        'Brand': ['Tesla', 'BMW', 'Tesla', 'Audi'],
        'Fuel_Type': ['Electric', 'Petrol', 'Electric', 'Diesel']
    }

    # Initialize the encoder
    encoder = FeatureEncoder(data=car_inventory)

    # 1. Select categorical columns to transform
    categorical_cols = ['Brand', 'Fuel_Type']

    # 2. Execute the encoding
    processed_features = encoder.encode_categories(categorical_cols)

    # Display Results
    print("--- Original Inventory ---")
    print(encoder)
    
    print("\n--- Encoded Feature Matrix (ML Ready) ---")
    print(processed_features)

if __name__ == "__main__":
    main()