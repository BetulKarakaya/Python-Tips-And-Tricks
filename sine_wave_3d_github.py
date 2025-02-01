import numpy as np
import matplotlib.pyplot as plt

class TrigonometricWaves:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    
    # Define the function to calculate Euclidean distance
    def distance_from_origin(self,x,y):
        return np.linalg.norm([x,y])  # sqrt(x^2 + y^2)

    def calculate_Z(self):
        
       # Vectorize the function to apply it element-wise on the grid
        vectorized_distance = np.vectorize(self.distance_from_origin)
        self.Z = vectorized_distance(self.X, self.Y)  # Compute the distance at each grid point
       
    
    def sine_wave(self):
        if not hasattr(self, 'Z'):
            raise ValueError("Z values are not computed yet. Call calculate_Z() first.")
        self.Z_sine_wave = np.sin(self.Z)  # Sinusoidal wave pattern

    
    def cosine_wave(self):
        if not hasattr(self, 'Z'):
            raise ValueError("Z values are not computed yet. Call calculate_Z() first.")
        self.Z_cosine_wave = np.cos(self.Z)  # Cosinusoidal wave pattern
    
    def vizualize(self):
        fig, axs = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={"projection": "3d"})
        
        # Common vmin and vmax for better color consistency
        vmin = min(self.Z_sine_wave.min(), self.Z_cosine_wave.min())
        vmax = max(self.Z_sine_wave.max(), self.Z_cosine_wave.max())

        surf1 = axs[0].plot_surface(self.X, self.Y, self.Z_sine_wave, cmap="viridis", vmin=vmin, vmax=vmax)
        axs[0].set_xlabel("X Axis")
        axs[0].set_ylabel("Y Axis")
        axs[0].set_title("Sine Wave Based on Distance from Origin", fontsize = 15)

        axs[1].plot_surface(self.X, self.Y, self.Z_cosine_wave, cmap="viridis", vmin=vmin, vmax=vmax)
        axs[1].set_xlabel("X Axis")
        axs[1].set_ylabel("Y Axis")
        axs[1].set_title("Cosine Wave Based on Distance from Origin", fontsize = 15)

        cbar_ax = fig.add_axes([0.95, 0.3, 0.01, 0.5])  # [left, bottom, width, height]
        fig.colorbar(surf1, cax=cbar_ax)  
        
        fig.subplots_adjust(wspace=0.4)

        plt.show()


    def app_main(self):
        self.calculate_Z()
        self.sine_wave()
        self.cosine_wave()
        self.vizualize()

def main():
    # Create a 100x100 grid of X and Y coordinates ranging from -5 to 5
    x = np.linspace(-5, 5, 100)  # X-axis values
    y = np.linspace(-5, 5, 100)  # Y-axis values
    X, Y = np.meshgrid(x, y)  # Create a coordinate grid
    
    app = TrigonometricWaves(X,Y)
    app.app_main()
   


if __name__ == "__main__":
    main()