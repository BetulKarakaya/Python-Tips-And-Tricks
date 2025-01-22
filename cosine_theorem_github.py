import math
import matplotlib.pyplot as plt
import numpy as np

class Triangle():
    def __init__(self, side_a, side_b, angle_degrees):
        self.side_a = side_a
        self.side_b = side_b
        self.angle_degrees = angle_degrees

    def calculate_side_c(self):

        # Convert angles to radians
        # Python's math library, including trigonometric functions (sin, cos, etc.), 
        # expect angles in radians, not degrees. 
        self.angle_radians = math.radians(self.angle_degrees)

        # Cosine Theory
        self.side_c = math.sqrt(self.side_a**2 + self.side_b**2 - 2 * self.side_a * self.side_b * math.cos(self.angle_radians))
    
    def verify_calculation(self):
        
        sin_value = math.sin(self.angle_radians)
        cos_value = math.cos(self.angle_radians)
        tan_value = math.tan(self.angle_radians)

        # Pythagorean Identity controls
        pythagorean_identity = sin_value**2 + cos_value**2

        print("\nVerification Results:")
        print(f"Sin({self.angle_degrees}°) = {sin_value:.4f}")
        print(f"Cos({self.angle_degrees}°) = {cos_value:.4f}")
        print(f"Tan({self.angle_degrees}°) = {tan_value:.4f}")
        print(f"Length of side c (using Law of Cosines) = {self.side_c:.4f}")
        print(f"Verification of Pythagorean Identity (Sin^2 + Cos^2): {pythagorean_identity:.4f}")

    def visualize(self):    
   
        try:
        
            # Determine the vertices of the triangle
            points_x = [0, self.side_b, self.side_a * math.cos(self.angle_radians)]
            points_y = [0, 0, self.side_a * math.sin(self.angle_radians)]

            # Draw the triangle
            # plt.plot([x coordinates], [y coordinates], color, length of side as a label)
            plt.figure(figsize=(6, 6))
            plt.plot([points_x[0], points_x[1]], [points_y[0], points_y[1]], 'r', label=f'side b = {self.side_b}')
            plt.plot([points_x[1], points_x[2]], [points_y[1], points_y[2]], 'g', label=f'side c = {self.side_c:.2f}')
            plt.plot([points_x[2], points_x[0]], [points_y[2], points_y[0]], 'b', label=f'side a = {self.side_a}')
            
            # Adjust triangle vertices and drawing details
            plt.scatter(points_x, points_y, color="black")
            plt.text(points_x[0], points_y[0], 'A', fontsize=12, color="black")
            plt.text(points_x[1], points_y[1], 'B', fontsize=12, color="black")
            plt.text(points_x[2], points_y[2], 'C', fontsize=12, color="black")
            
            plt.title("Triangle Visualization")
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.axhline(0, color="black",linewidth=0.5)
            plt.axvline(0, color="black",linewidth=0.5)
            plt.grid(color = "gray", linestyle = "--", linewidth = 0.5)
            plt.legend()
            plt.show()
        
        except ImportError:
            print("Matplotlib or NumPy is not installed. Install them to visualize the triangle.")

def main():
    try:
        side_a = float(input("Enter the length of side a: "))
        side_b = float(input("Enter the length of side b: "))
        angle_degrees = float(input("Enter the angle between them in degrees: "))

        triangle = Triangle(side_a = side_a, side_b = side_b, angle_degrees = angle_degrees)
        triangle.calculate_side_c()
        triangle.verify_calculation()
        triangle.visualize()

    except:
        raise ValueError("Please Enter Integer Values")

if __name__ == "__main__":
    main()