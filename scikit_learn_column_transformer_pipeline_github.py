import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

class HousePricePredictor:
    def __init__(self):
        # Pipeline for Numerical Data (Fill Missing + Scale)
        self.numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')), # Fill NaNs with median
        ('scaler', StandardScaler())                   # Normalize data
    ])
        # Pipeline for Categorical Data (Fill Missing + Encode)
        self.categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
        
    def preprocessing(self,numerical_columns:None,categorical_columns:None):
        # Merging Paths with ColumnTransformer
        # Mapping which pipeline goes to which specific columns
        self.preprocessor = ColumnTransformer(
            transformers=[
                ('num', self.numeric_transformer, numerical_columns),
                ('cat', self.categorical_transformer, categorical_columns)
            ]
        )

    def create_model_pipeline(self):
        # Full Pipeline: Preprocessing + Model (Random Forest)
        self.full_model = Pipeline(steps=[
            ('preprocessor', self.preprocessor),
            ('regressor', RandomForestRegressor())
        ])
        return self.full_model

def main():
    # Create a Realistic Dataset
    # Includes missing values (NaN) and categorical text
    data = {
        'sq_meters': [120, 85, np.nan, 150, 200, 110], 
        'rooms': [2, 1, 2, 3, 4, 2],
        'neighborhood': ['Beykoz', 'Besiktas', 'Beykoz', 'Besiktas', 'Kadikoy', np.nan], 
        'building_age': [5, 20, 15, 2, 30, 10],
        'price': [5000, 4200, 4800, 7500, 7100, 5200] # Target variable
    }

    numerical_cols = ["sq_meters","rooms","building_age"]
    categorical_cols = ["neighborhood"]

    df = pd.DataFrame(data)
    X = df.drop('price', axis=1)
    y = df['price']

    predictor = HousePricePredictor()
    predictor.preprocessing(numerical_columns=numerical_cols,categorical_columns=categorical_cols)
    
    # Create model
    full_model = predictor.create_model_pipeline()
    # Train and Predict
    full_model.fit(X, y)
    print("--- Model Trained Successfully! ---")

    # Predicting for a brand new house (Raw Data)
    new_house = pd.DataFrame({
        'sq_meters': [130],
        'rooms': [3],
        'neighborhood': ['Beykoz'],
        'building_age': [7]
    })

    prediction = full_model.predict(new_house)
    print(f"Predicted Price for New House: {prediction[0]:.2f} TL")

if __name__ == "__main__":
    main()