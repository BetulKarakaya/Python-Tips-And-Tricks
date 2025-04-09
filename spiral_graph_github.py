import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class SpiralGraph:
    def __init__(self, num_points=1000):
        self.num_points = num_points
        self.theta = np.linspace(0, 4 * np.pi, self.num_points)  # Angle from 0 to 4*pi
        self.r = self.theta ** 2  # Radius increases as the square of the angle
        
        # Polar to Cartesian coordinates
        self.x = self.r * np.sin(self.theta)
        self.y = self.r * np.cos(self.theta)
        
        # Generate a color map based on the angle
        self.colors = cm.viridis(self.theta / max(self.theta))  # Color map (viridis)

    def plot_spiral(self):
        plt.figure(figsize=(8, 8))
        plt.scatter(self.x, self.y, c=self.colors, s=10, alpha=0.7)
        plt.title('Spiral Graph with Dynamic Colors', fontsize=14)
        plt.axis('off')  # Hide axis for cleaner look
        plt.show()

def main():
    
    spiral = SpiralGraph()
    spiral.plot_spiral()

if __name__ == "__main__":
    main()
