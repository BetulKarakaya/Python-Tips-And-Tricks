import numpy as np
import matplotlib.pyplot as plt

class CoffeeSalesPredictor:
    
    def __init__(self, days, sales):
        """ Initialize the model with historical sales data """
        self.days = np.array(days).reshape(-1, 1)  # Reshape to column vector
        self.sales = np.array(sales)
        
        # Compute the trend using Least Squares Method (Simple Linear Regression)
        ones = np.ones((self.days.shape[0], 1))  # Add intercept (bias term)
        X = np.hstack((ones, self.days))  # Stack ones and days
        
        # Calculate regression coefficients (m and b)
        self.coefficients = np.linalg.inv(X.T @ X) @ X.T @ self.sales
        self.b, self.m = self.coefficients[0], self.coefficients[1]

    def predict(self, future_days):
        """ Predict coffee sales for given future days """
        future_days = np.array(future_days).reshape(-1, 1)
        ones = np.ones((future_days.shape[0], 1))  # Add intercept
        X_future = np.hstack((ones, future_days))
        return X_future @ self.coefficients

    def visualize(self):
        """ Visualize the historical data and the trend line """
        plt.scatter(self.days, self.sales, color='brown', label="Real Sales Data")
        predicted_sales = self.predict(self.days)
        plt.plot(self.days, predicted_sales, color='orange', label="Trend Line")
        
        plt.xlabel("Days")
        plt.ylabel("Coffee Sales")
        plt.title("Coffee Sales Prediction")
        plt.legend()
        plt.grid(True)
        plt.show()



def main():
    # Simulated real-world coffee sales data (e.g., sales over 10 days)
    days = np.arange(1, 11)  # Days from 1 to 10
    sales = np.array([50, 55, 53, 60, 65, 68, 72, 70, 75, 78])  # Coffee sales per day

    # Create predictor
    predictor = CoffeeSalesPredictor(days, sales)
    predictor.visualize()

    # Predict sales for future days
    future_days = [11, 12, 13, 14, 15]
    predicted_sales = predictor.predict(future_days)

    print(f"Predicted coffee sales for future days {future_days}: {np.round(predicted_sales, 2)} ☕")


if __name__ == "__main__":
    main()