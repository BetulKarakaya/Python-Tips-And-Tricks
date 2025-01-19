import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_hypotenuse(a,b):
    
    hypotenuse = math.hypot(a, b)
    print(f"The hypotenuse of the triangle is: {hypotenuse:.4f}")

def visualize_triangle(a,b):
   
    triangle_points = np.array([
        [0, 0], # Starting point of the triangle
        [a, 0], # The other end of the base of the triangle
        [0, b], # Height of triangle
        [0, 0], # Return to starting point to close triangle
    ])

    
    plt.figure(figsize=(8, 6))
    plt.plot(triangle_points[:, 0], triangle_points[:, 1], marker='o', color='black', label="Triangle sides")
    plt.fill(triangle_points[:, 0], triangle_points[:, 1], color='skyblue', alpha=0.3, label="Triangle Area")  # Üçgenin içini renklendirme

    
    plt.title("Right Triangle with Hypotenuse")
    plt.xlabel("Base (a)")
    plt.ylabel("Height (b)")
    plt.gca().set_aspect("equal", adjustable="box") #Equal Scaling  
    plt.grid(True)
    plt.axhline(0, color="black",linewidth=0.5)
    plt.axvline(0, color="black",linewidth=0.5)
    plt.legend()
    plt.show()


def main():

    print("Welcome To Right Triangle Hypotenuse Calculator".center(80,"-"))

    a = float(input("Enter side a of the triangle (base): "))
    b = float(input("Enter side b of the triangle (height): "))

    calculate_hypotenuse(a,b)
    visualize_triangle(a,b)

if __name__ == "__main__":
    main()