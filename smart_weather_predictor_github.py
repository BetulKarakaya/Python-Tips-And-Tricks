import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

class SmartWeatherPredictor:
    
    def __init__(self, days, temperatures, degree=3):
        """ Initialize polynomial regression model for temperature prediction """
        self.days = np.array(days)
        self.temperatures = np.array(temperatures)
        self.degree = degree
        
        # Fit polynomial regression model
        self.coeffs = np.polyfit(self.days, self.temperatures, self.degree)
        self.model = Polynomial(self.coeffs[::-1])  # Reverse coefficients for Polynomial class

    def predict(self, future_days):
        """ Predict temperatures for given future days """
        future_days = np.array(future_days)
        return self.model(future_days)

    def visualize(self):
        """ Plot real temperature data and the polynomial regression curve """
        plt.scatter(self.days, self.temperatures, color='blue', label="Actual Temperatures")
        x_range = np.linspace(min(self.days), max(self.days) + 5, 100)
        plt.plot(x_range, self.model(x_range), color='red', label="Polynomial Trend")

        plt.xlabel("Days")
        plt.ylabel("Temperature (°C)")
        plt.title("🌡️ Temperature Prediction with Polynomial Regression")
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    days = np.arange(1, 11)  
    temperatures = np.array([15, 16, 14, 17, 20, 22, 23, 25, 28, 30])  

    predictor = SmartWeatherPredictor(days, temperatures, degree=3)
    predictor.visualize()

    future_days = [11, 12, 13, 14, 15]
    predicted_temperatures = predictor.predict(future_days)
    print(f"🌡️ Predicted temperatures for future days {future_days}: {np.round(predicted_temperatures, 2)} °C")

if __name__ == "__main__":
    main()
