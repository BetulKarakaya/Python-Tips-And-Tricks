import numpy as np
import matplotlib.pyplot as plt


# Define a function to calculate the Euclidean distance from the origin (0,0)
def distance_from_origin(x, y):
    return np.linalg.norm([x, y])  # Uses NumPy's linear algebra norm function


def visualize(X,Y,Z):
    # Plot the 3D surface
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
   
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Distance from Origin")
    ax.set_title("3D Distance from Origin Visualization")
    plt.show()
def main():
    # Create a grid of (x, y) coordinates using NumPy's meshgrid
    x = np.linspace(-5, 5, 100)  # 100 points from -5 to 5
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)  # Creates a coordinate matrix

    """ 
    np.vectorize() converts the function into a form that can operate element-wise on NumPy arrays.
    Instead of looping through individual (x, y) pairs, it applies the function efficiently to the entire grid.
    This speeds up computations compared to a traditional for-loop.
    """
    # Vectorize the function to apply it element-wise on the grid
    vectorized_distance = np.vectorize(distance_from_origin)
    Z = vectorized_distance(X, Y)  # Compute the distance at each grid point
    
    visualize(X,Y,Z)

if __name__ == "__main__":
    main()