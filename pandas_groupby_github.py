import pandas as pd

class SalesSummary:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("❌ Input must be a pandas DataFrame.")
        self.df = df


    # Group the DataFrame by the 'Category' column and apply multiple aggregation functions (count, sum, mean)
    # to the 'Sales' column, which gives us how many items were sold, the total sales amount,
    # and the average sales per item for each product category.

    def summarize_sales(self):
        print("📊 Category-based sales summary:\n")
        summary = self.df.groupby("Category")["Sales"].agg(["count", "sum", "mean"])
        print(summary)

def main():
    data = {
        "Product": ["Cake", "Bread", "Muffin", "Croissant", "Pie", "Baguette"],
        "Category": ["Pastry", "Bread", "Pastry", "Pastry", "Pastry", "Bread"],
        "Sales": [120, 80, 90, 150, 110, 95]
    }

    df = pd.DataFrame(data)
    summary = SalesSummary(df)
    summary.summarize_sales()

if __name__ == "__main__":
    main()
