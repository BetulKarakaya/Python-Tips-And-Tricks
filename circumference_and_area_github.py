import math
import matplotlib.pyplot as plt
import numpy as np

def calc_circumference(radius):
    return 2 * math.pi * radius

def calc_area(radius):
    return math.pi * math.pow(radius, 2)

def visualize_circle(radius):
     
    theta = [i * 0.01 for i in range(0, int(2 * math.pi / 0.01) + 1)]  # Angle values ​​from 0 to 2π
    x = [radius * math.cos(t) for t in theta]  # X coordinates
    y = [radius * math.sin(t) for t in theta]  # Y coordinates

    plt.figure(figsize=(6, 6))
    
    plt.plot(x, y, label = f"Circle with radius {radius}", color = "blue") 
    plt.scatter(0, 0, color = "red", label="Center (0, 0)")  # Mark the center point
    
    plt.title("Circle Visualization", fontsize=14)
   
    plt.xticks(np.arange(-1*(radius), radius +1, 1))
    plt.yticks(np.arange(-1*(radius), radius +1, 1))
    
    plt.gca().set_aspect("equal")  # Synchronize scaling rate
    
    plt.grid(True)
    plt.gca().set_axisbelow(True)
    
    plt.legend()
    plt.show()

def main():
    print("Welcome To Calculator the Circumference and Area of ​​a Circle".center(100, "-"))
    radius = float(input("Enter the radius of the circle: "))

    circumference = calc_circumference(radius = radius)
    area = calc_area(radius = radius)

    print(f"The circumference of the circle is: {circumference:.4f}")
    print(f"The area of the circle is: {area:.4f}")

    visualize_circle(radius = radius)

if __name__ == "__main__":
    main()