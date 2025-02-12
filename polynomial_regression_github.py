import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

class BreadSalesPredictor:
    
    def __init__(self, weeks, sales, degree=3):
        """ Initialize the model with historical sales data and fit a polynomial regression """
        self.weeks = np.array(weeks)
        self.sales = np.array(sales)
        self.degree = degree  # Degree of the polynomial regression

        # Fit a polynomial regression model
        self.poly_coefficients = Polynomial.fit(self.weeks, self.sales, self.degree)
    
    def predict(self, future_weeks):
        """ Predict bread sales for given future weeks """
        future_weeks = np.array(future_weeks)
        return self.poly_coefficients(future_weeks)

    def visualize(self, future_weeks, future_sales):
        """ Visualize the historical data and the polynomial trend """
        plt.scatter(self.weeks, self.sales, color='brown', label="Real Sales Data")  # Actual data points
        plt.plot(self.weeks, self.poly_coefficients(self.weeks), color='orange', label="Trend Line")  # Fitted polynomial
        
        
        plt.scatter(future_weeks, future_sales, color='red', label="Predicted Sales", marker="x")  # Predictions

        plt.xlabel("Weeks")
        plt.ylabel("Bread Sales")
        
        plt.title("Bread Sales Prediction with Polynomial Regression")
        plt.legend()
        
        plt.yticks(np.arange(0, max(future_sales)+1, 50))
        
        plt.grid(True)
        plt.gca().set_axisbelow(True)
        plt.show()

def main():
    # Simulated real-world bakery sales data 
    weeks = np.arange(1, 11)  # Weeks from 1 to 10
    sales = np.array([100, 120, 150, 180, 250, 300, 400, 450, 500, 550])  # Bread sales per week

    # Create predictor
    predictor = BreadSalesPredictor(weeks, sales, degree=3)
    future_weeks = [11, 12, 13, 14, 15]  # Predict next 5 weeks
    future_sales = predictor.predict(future_weeks)
    predictor.visualize(future_weeks = future_weeks, future_sales= future_sales)

    predicted_sales = predictor.predict(future_weeks)
    print(f"Predicted bread sales for future weeks {future_weeks}: {np.round(predicted_sales, 2)} 🥖")

if __name__ == "__main__":
    main()
