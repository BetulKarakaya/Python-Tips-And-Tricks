import pandas as pd

class DataReshaper:
    """
    A class to handle DataFrame reshaping and unpivoting 
    for improved analytical workflows.
    """
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def __str__(self):
        return f"Original (Wide) Format:\n{self.df.to_string()}"

    def unpivot_monthly_data(self, id_vars, value_vars, var_name='Month', value_name='Revenue'):
        """
        Converts wide-format monthly columns into a long-format 
        tidy dataset using the melt method.
        """
        # TRICK: melt() consolidates multiple columns into two: a label and a value
        long_df = pd.melt(
            self.df, 
            id_vars=id_vars, 
            value_vars=value_vars, 
            var_name=var_name, 
            value_name=value_name
        )
        return long_df

def main():
    # Sample Dataset: Wide format (One column per month)
    # This format is easy for humans to read but hard for computers to plot
    quarterly_sales = {
        'Product': ['Laptop', 'Tablet'],
        'Jan_Sales': [100, 50],
        'Feb_Sales': [120, 60],
        'Mar_Sales': [150, 70]
    }

    # Initialize the reshaper
    reshaper = DataReshaper(data=quarterly_sales)

    # 1. Define which column stays (id_vars) and which columns disappear (value_vars)
    fixed_col = ['Product']
    monthly_cols = ['Jan_Sales', 'Feb_Sales', 'Mar_Sales']

    # 2. Execute the unpivot
    tidy_data = reshaper.unpivot_monthly_data(id_vars=fixed_col, value_vars=monthly_cols)

    # Display Results
    print(reshaper)
    print("\n--- Reshaped (Long) Format ---")
    print(tidy_data.sort_values(by='Product'))

if __name__ == "__main__":
    main()