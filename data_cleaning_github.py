import numpy as np
import pandas as pd
import time

class Inventory:
    
    def __init__(self):
        
        self.data = {
            "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Smartphone", "Tablet"],
            "Price": [1000, 50, 80, None, 150, None, 400], 
            "Stock": [10, 50, 30, 15, None, 25, None],  
            "Rating": [4.5, None, 4.0, 4.8, None, 4.2, 3.9]  
        }

        self.df = pd.DataFrame(self.data)

    def get_df(self):
        return self.df.copy()  # We preserve the original data by returning a copy on each call.

    def report_missing_data(self):
       
        missing_info = self.df.isnull().sum()
        total_rows = len(self.df)
        
        report = pd.DataFrame({
            "Missing Values": missing_info,
            "Missing (%)": (missing_info / total_rows) * 100
        })

        report = report[report["Missing Values"] > 0] 
        
        if report.empty:
            print("No missing values in the dataset!")
        else:
            print("\nMissing Data Overview:\n", report)
            print("\nColumn with Most Missing Data:", report["Missing Values"].idxmax())
    
    def fill_missing_data_pandas(self, df):
       
        df["Price"] = df["Price"].fillna(df["Price"].median()) 
        df["Stock"] = df["Stock"].fillna(df["Stock"].mean())  
        df["Rating"] = df["Rating"].fillna(df.groupby("Product")["Rating"].transform("mean"))
        df["Rating"] = df["Rating"].fillna(df["Rating"].median())  # If there is still NaN, fill with the general median
        return df

    def fill_missing_data_numpy(self, df):
        
        df["Price"] = np.where(df["Price"].isnull(), df["Price"].median(), df["Price"])
        df["Stock"] = np.where(df["Stock"].isnull(), df["Stock"].mean(), df["Stock"])
        df["Rating"] = np.where(df["Rating"].isnull(), df["Rating"].median(), df["Rating"])
        return df


def main():
    app = Inventory()
    
    print("\nRaw Data\n\n", app.get_df())
    print("\nRunning Missing Data Report...")
    app.report_missing_data()

    print("\nRunning Pandas Fill Method...")
    start_time = time.time()
    filled_df_pandas = app.fill_missing_data_pandas(app.get_df())
    pandas_time = time.time() - start_time
    print(f"Time Taken with Pandas: {pandas_time:.6f} seconds")

    print("\nRunning NumPy Fill Method...")
    start_time = time.time()
    filled_df_numpy = app.fill_missing_data_numpy(app.get_df())
    numpy_time = time.time() - start_time
    print(f"Time Taken with NumPy: {numpy_time:.6f} seconds")

    print("\nCleaned Data with Pandas:\n", filled_df_pandas.to_string())
    print("\nCleaned Data with NumPy:\n", filled_df_numpy.to_string())

if __name__ == "__main__":
    main()
