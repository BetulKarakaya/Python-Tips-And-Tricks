import pandas as pd

class SalesDataAnalysis:
    """
    A class to perform statistical analysis on employee sales data 
    using Pandas label-based indexing.
    """
    def __init__(self, data):
        # Setting 'Employee' as the index is crucial for returning names instead of row numbers
        self.df = pd.DataFrame(data).set_index('Employee')

    def __str__(self):
        return self.df.to_string()

    def get_top_performer_per_month(self):
        """Returns the employee with the highest sales for each month."""
        return self.df.idxmax(axis=0)
    
    def get_best_month_per_employee(self):
        """Returns the most successful month for each individual employee."""
        return self.df.idxmax(axis=1)
    
    def get_worst_month_per_employee(self):
        """Returns the month with the lowest sales for each individual employee."""
        return self.df.idxmin(axis=1)

def main():
    # Sample Dataset (Monthly sales per employee)
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
        'January': [15000, 18000, 12000, 17000],
        'February': [16000, 14000, 21000, 19000],
        'March': [13000, 25000, 19000, 22000] 
    }
    
    # Initialize the analysis object
    analysis = SalesDataAnalysis(data=data)

    # Executing analysis methods
    top_performers = analysis.get_top_performer_per_month()
    best_months = analysis.get_best_month_per_employee()
    worst_months = analysis.get_worst_month_per_employee()

    # Displaying results
    print("--- Monthly Sales Data Matrix ---")
    print(analysis)
    
    print("\n--- Top Performer per Month (Who sold the most?) ---")
    print(top_performers)
    
    print("\n--- Best Month per Employee (Personal Records) ---")
    print(best_months)
    
    print("\n--- Worst Month per Employee (Areas for Improvement) ---")
    print(worst_months)

if __name__ == "__main__":
    main()