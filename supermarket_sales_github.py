import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SupermarketSales:
    
    def __init__(self):
        
        self.data = {
            "Product": ["Milk", "Bread", "Eggs", "Cereal", "Juice"],
            "Price": [1.5, 1.0, 0.2, 3.5, 2.0],  # Price per unit ($)
            "Daily_Sales": [
                [np.nan, 100, 150, 80, 90],   # Monday
                [120, np.nan, 140, 85, np.nan],  # Tuesday
                [130, 105, np.nan, 95, 110],  # Wednesday
                [np.nan, 110, 160, np.nan, 120],  # Thursday
                [140, 120, 170, 90, 130]  # Friday
            ]
        }
        
        self.df = pd.DataFrame(self.data["Daily_Sales"], columns=self.data["Product"])
        self.df.index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.prices = pd.Series(self.data["Price"], index=self.data["Product"])

    def fill_missing_data(self):
        print(self.df)
        self.df.fillna(self.df.mean(), inplace=True)
    
    def calculate_revenue(self):
        
        self.revenue = self.df.sum() * self.prices
    
    def display_summary(self):
       
        print("\n📊 Supermarket Sales Analysis:")
        print("------------------------------------------------")
        print(f"Best-selling product: {self.df.sum().idxmax()} ({self.df.sum().max()} units sold)")
        print(f"Least-selling product: {self.df.sum().idxmin()} ({self.df.sum().min()} units sold)")
        print(f"Total revenue: ${self.revenue.sum():.2f}")
        print(f"Lowest revenue product: {self.revenue.idxmin()} (${self.revenue.min():.2f})")
        print(f"Highest revenue product: {self.revenue.idxmax()} (${self.revenue.max():.2f})")
        print("------------------------------------------------\n")

    def visualization(self):

        colors = ["#81a4f7", "#f7a481", "#b081f7", "#faa946", "#81f7a4"]
        fig, axes = plt.subplots(1,2,figsize=(15, 8))
        axes[0].bar(self.df.columns,self.df.sum(), color = colors )
        axes[0].set_title("Total Sales per Product", fontsize=18, color="#393d47", weight="bold")
        axes[0].set_xlabel("Product")
        axes[0].set_ylabel("Total Units Sold")
        axes[0].grid()
        axes[0].set_axisbelow(True)
        
        axes[1].bar(self.data["Product"],self.data["Price"], color = colors)
        axes[1].set_title("Price Of Product", fontsize=18, color="#393d47", weight="bold")
        axes[1].set_xlabel("Product")
        axes[1].set_ylabel("Price")
        axes[1].grid()
        axes[1].set_axisbelow(True)
        
        fig.text(
            0.5,
            0.05,
            f"Best-selling product: {self.df.sum().idxmax()} ({self.df.sum().max()} units sold)\n"
            f"Least-selling product: {self.df.sum().idxmin()} ({self.df.sum().min()} units sold)\n"
            f"Total revenue: ${self.revenue.sum():.2f}\n"
            f"Lowest revenue product: {self.revenue.idxmin()} (${self.revenue.min():.2f})\n"
            f"Highest revenue product: {self.revenue.idxmax()} (${self.revenue.max():.2f})",
            ha="center", va="bottom", fontsize=14, color="#393d47"
        )
        plt.subplots_adjust(left=0.1, right=0.9, bottom=0.3, top=0.92, wspace=0.4, hspace=0.4)
        plt.show()

    def run(self):
       
        self.fill_missing_data()
        self.calculate_revenue()
        self.display_summary()
        self.visualization()


def main():
    app = SupermarketSales()
    app.run()


if __name__ == "__main__":
    main()
