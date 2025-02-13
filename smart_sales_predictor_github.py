import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

class SmartSalesPredictor:
    
    def __init__(self, weeks, sales, degree=3):
        """ Initialize polynomial regression model with given degree """
        self.weeks = np.array(weeks)
        self.sales = np.array(sales)
        self.degree = degree
        
        # Fit polynomial regression model
        self.coeffs = np.polyfit(self.weeks, self.sales, self.degree)
        self.model = Polynomial(self.coeffs[::-1])  # Reverse coefficients for Polynomial class

    def predict(self, future_weeks):
        """ Predict sales for given future weeks """
        future_weeks = np.array(future_weeks)
        return self.model(future_weeks)

    def visualize(self):
        """ Plot real sales data and the polynomial regression curve """
        plt.scatter(self.weeks, self.sales, color='blue', label="Actual Sales")
        x_range = np.linspace(min(self.weeks), max(self.weeks) + 5, 100)
        plt.plot(x_range, self.model(x_range), color='red', label="Polynomial Trend")

        plt.xlabel("Weeks")
        plt.ylabel("Sales")
        plt.title("📈 Sales Prediction with Polynomial Regression")
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    weeks = np.arange(1, 11)  
    sales = np.array([50, 55, 54, 60, 68, 75, 85, 95, 105, 120])  

    predictor = SmartSalesPredictor(weeks, sales, degree=3)
    predictor.visualize()

    future_weeks = [11, 12, 13, 14, 15]
    predicted_sales = predictor.predict(future_weeks)
    print(f"📊 Predicted sales for future weeks {future_weeks}: {np.round(predicted_sales, 2)}")

if __name__ == "__main__":
    main()
