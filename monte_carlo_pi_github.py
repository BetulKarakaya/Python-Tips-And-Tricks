import numpy as np
import matplotlib.pyplot as plt

class MonteCarloPi:
    def __init__(self, num_samples=10000):
        """ Initialize the simulation with a number of random samples """
        self.num_samples = num_samples
        self.inside_circle = 0  # Count of points inside the unit circle
        self.points = None  # Store generated points

    def calculate_pi(self):
        """ Run the Monte Carlo simulation to estimate pi """
        # Generate random points in the range [-1, 1] x [-1, 1]
        x = np.random.uniform(-1, 1, self.num_samples)
        y = np.random.uniform(-1, 1, self.num_samples)
        
        # Compute distances from the origin (0,0)
        distances = np.sqrt(x**2 + y**2)
        
        # Count points inside the unit circle
        self.inside_circle = np.sum(distances <= 1)
        self.points = (x, y)
        
        # Estimate pi using the ratio of points inside the circle to total points
        return (self.inside_circle / self.num_samples) * 4

    def visualize(self):
        """ Visualize the Monte Carlo method with a scatter plot """
        x, y = self.points
        
        # Separate points inside and outside the circle
        inside = (x**2 + y**2) <= 1
        
        plt.figure(figsize=(6,6))
        plt.scatter(x[inside], y[inside], color='blue', s=1, label='Inside Circle')
        plt.scatter(x[~inside], y[~inside], color='red', s=1, label='Outside Circle')
        
        # Draw the unit circle
        circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
        plt.gca().add_patch(circle)
        
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
        plt.gca().set_aspect('equal', adjustable='datalim')
        plt.title("Monte Carlo π Estimation")
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    num_samples = 10000 
    mc = MonteCarloPi(num_samples)
    estimated_pi = mc.calculate_pi()
    print(f"Estimated π with {num_samples} samples: {estimated_pi:.6f}")
    mc.visualize()

if __name__ == "__main__":
    main()
