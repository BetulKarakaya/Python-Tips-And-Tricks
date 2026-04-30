import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

class DataArchitect:
    """
    Establishes a centralized architecture that processes 
    different data types simultaneously.
    """
    def __init__(self):
        # For numerical columns: Standardization (Mean=0, Std=1)
        self.num_transformer = StandardScaler()
        # For categorical columns: One-Hot (Split into 0s and 1s)
        self.cat_transformer = OneHotEncoder(handle_unknown='ignore')

    def get_preprocessor(self, num_cols, cat_cols):
        """
        TRICK: ColumnTransformer
        This is where we 'map' which transformation goes to which column.
        """
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.num_transformer, num_cols),
                ('cat', self.cat_transformer, cat_cols)
            ]
        )
        return preprocessor

def main():

    df = pd.DataFrame({
        'age': [25, 32, 47, 51],
        'salary': [50000, 80000, 120000, 100000],
        'city': ['London', 'Paris', 'Istanbul', 'London']
    })

    # Define column types
    num_features = ['age', 'salary']
    cat_features = ['city']

    # Initialize our architect and transform the data
    architect = DataArchitect()
    preprocessor = architect.get_preprocessor(num_features, cat_features)
   
    processed_data = preprocessor.fit_transform(df)

    cat_names = preprocessor.named_transformers_['cat'].get_feature_names_out(cat_features)
    all_cols = num_features + list(cat_names)
    
    print("--- Scikit-Learn ColumnTransformer Result ---")
    print(pd.DataFrame(processed_data, columns=all_cols).round(2))

if __name__ == "__main__":
    main()