import numpy as np
import matplotlib.pyplot as plt

class TrigFunctions:
    def __init__(self, start=-2*np.pi, end=2*np.pi, num_points=100):
        """
        Initialize the class with a range of x values.
        
        Parameters:
        - start: Start of the interval (default: -2π)
        - end: End of the interval (default: 2π)
        - num_points: Number of points to generate
        """
        self.x = np.linspace(start, end, num_points)  # Generate x values
        self.sin_y = np.sin(self.x)  # Compute sine values
        self.cos_y = np.cos(self.x)  # Compute cosine values
        self.tan_y = np.tan(self.x)  # Compute tangent values
    
    def visualize(self):
        """
        Plot the sine, cosine, and tangent functions.
        """
        plt.figure(figsize=(12, 5))
        plt.plot(self.x, self.sin_y, label="sin(x)", color="#ff5733", linestyle="--")
        plt.plot(self.x, self.cos_y, label="cos(x)", color="#33ff57", linestyle="-")
        plt.plot(self.x, self.tan_y, label="tan(x)", color="#3357ff", linestyle=":")
        
        # Avoid extreme tangent values
        plt.ylim(-2, 2)
        
        plt.axhline(0, color="black", linewidth=0.8)
        plt.axvline(0, color="black", linewidth=0.8)
        plt.title("Trigonometric Functions")
        plt.xlabel("x values (radians)")
        plt.ylabel("Function values")
        plt.legend()
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.gca().set_axisbelow(True)
        plt.show()

def main():
    trig_plot = TrigFunctions()
    trig_plot.visualize()

if __name__ == "__main__":
    main()
