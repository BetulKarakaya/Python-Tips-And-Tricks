import pandas as pd
import numpy as np

class DataSanitizer:
    """
    A class to handle data cleaning and outlier management 
    using vectorized numerical constraints.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Sanitizer active for {len(self.df)} data points."

    def cap_outliers(self, column, lower_limit, upper_limit):
        """
        TRICK: np.clip()
        Instead of complex filtering, this forces all values to stay 
        within the [lower_limit, upper_limit] range.
        """
        # Values below lower_limit become lower_limit
        # Values above upper_limit become upper_limit
        self.df[f'{column}_Clean'] = np.clip(
            self.df[column], 
            a_min=lower_limit, 
            a_max=upper_limit
        )
        return self.df

def main():
    # Sample Dataset: Sensor readings with some impossible noise
    # (e.g., Temperature readings where 1000 is an error)
    data = {
        'Sensor_ID': [1, 2, 3, 4, 5],
        'Temperature': [22.5, -50.0, 24.1, 1000.0, 23.8] # -50 and 1000 are outliers
    }

    # Initialize the sanitizer
    sanitizer = DataSanitizer(data=data)

    # Define reasonable boundaries for a room temperature sensor
    clean_data = sanitizer.cap_outliers('Temperature', lower_limit=15.0, upper_limit=35.0)

    # Display Results
    print("--- Sensor Data Sanitization ---")
    print(clean_data)

if __name__ == "__main__":
    main()