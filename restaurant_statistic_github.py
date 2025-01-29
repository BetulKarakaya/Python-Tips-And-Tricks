import statistics
import random
import matplotlib.pyplot as plt
import numpy as np

class Restaurant:
    def __init__(self,daily_customers):
        self.daily_customers = daily_customers
    
    def calculate_statistic(self):
        # Calculate key statistical metrics
        self.mean_customers = statistics.mean(self.daily_customers)  
        self.median_customers = statistics.median(self.daily_customers)  
        self.mode_customers = statistics.mode(self.daily_customers) if len(set(self.daily_customers)) < len(self.daily_customers) else "No Mode"  
        self.std_dev_customers = statistics.stdev(self.daily_customers)  # Measures variation from the average
    
    def print_statistical_info(self):
        print("📊 Restaurant Customer Analysis (30 Days) 📊")
        print(f"Mean (Average): {self.mean_customers:.2f} customers/day")
        print(f"Median: {self.median_customers} customers/day")
        print(f"Mode: {self.mode_customers} customers/day")
        print(f"Standard Deviation: {self.std_dev_customers:.2f} (Customer variation)")

    def visualize(self):
        # Plot the data to visualize customer distribution
        plt.figure(figsize=(10, 5))
        plt.bar(range(1, 31),self.daily_customers,color="skyblue")
        
        plt.axhline(self.median_customers, color = "navy", linestyle= "dashed", linewidth=2, label=f'Median: {self.median_customers}')
        plt.axhline(self.mean_customers, color = "red", linestyle= "dashed", linewidth=2, label=f'Mean: {self.mean_customers}')
        
        plt.xticks(range(1,31))
        
        plt.ylabel("Number of Customers")
        plt.title("Daily Customers Over a Month")
        
        plt.grid()
        plt.gca().set_axisbelow(True)
        plt.legend(loc="upper right")
        plt.show()

def main():
    random.seed(42)
    restaurant = Restaurant([random.randint(0, 200) for _ in range(30)])
    restaurant.calculate_statistic()
    restaurant.print_statistical_info()
    restaurant.visualize()

if __name__ == "__main__":
    main()