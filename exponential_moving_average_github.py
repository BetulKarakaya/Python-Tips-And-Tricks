import numpy as np
import matplotlib.pyplot as plt

class ExponentialMovingAverage:
    
    def __init__(self, data, alpha=0.1):
        self.data = data
        self.alpha = alpha
    
    def exponential_moving_average(self):
        """
        Compute the Exponential Moving Average (EMA) of a given 1D data array.
        
        Parameters:
            data (array-like): The input data series.
            alpha (float): Smoothing factor (0 < alpha ≤ 1), higher means more weight on recent values.
        
        Returns:
            np.ndarray: The EMA series.
        """
        self.ema = np.zeros_like(self.data, dtype=float)  
        self.ema[0] = self.data[0]  
        
        for t in range(1, len(self.data)):
            self.ema[t] = self.alpha * self.data[t] + (1 - self.alpha) * self.ema[t - 1]  
        
        return self.ema  


def visualize_all(data, alpha_values, ema_result):
    plt.plot(data, marker="o", label="Original Data", linestyle="--", color="gray")
    
    for alpha, ema in zip(alpha_values, ema_result):
        plt.plot(ema, marker="s", label=f"EMA (alpha={alpha})")

    plt.title("Exponential Moving Average (EMA)")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    
    
    data = np.array([10, 15, 20, 18, 25, 30, 28, 35, 40, 38])

    alpha_values = [0.1, 0.3, 0.6]
    ema_result = []  

    for i, alpha in enumerate(alpha_values):
        app = ExponentialMovingAverage(data=data, alpha=alpha)
        ema = app.exponential_moving_average()  
        ema_result.append(ema)
        print(f"\nEMA with alpha={alpha}: {np.round(ema, 2)}")

    visualize_all(data=data, alpha_values=alpha_values, ema_result=ema_result)


if __name__ == "__main__":
    main()
