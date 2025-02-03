import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError("Coordinates must be numbers.")
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
class ShoelaceTheorem:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.points = points
        self.shoelace_points = self.points + [self.points[0]]  # Closing the polygon
        self.area = None
    
    def calculate_area(self):
        left_calc = sum(self.shoelace_points[i].x * self.shoelace_points[i + 1].y for i in range(len(self.points)))
        right_calc = sum(self.shoelace_points[i].y * self.shoelace_points[i + 1].x for i in range(len(self.points)))
        self.area = 0.5 * abs(right_calc - left_calc)
    
    def visualize(self):
        x_values = [p.x for p in self.shoelace_points]
        y_values = [p.y for p in self.shoelace_points]
        
        plt.figure(figsize=(10,10))
        plt.plot(x_values, y_values, marker='o', linestyle='-', color= "#0b048a", markersize=8, label="Polygon")
        for i, p in enumerate(self.points):
            plt.text(p.x, p.y, f' P{i} ', fontsize=12, color="#25243d", verticalalignment="bottom")
        
        plt.text(.01, .99, f"Area of polygon is : {self.area}", size = 12, color="#25243d", ha = "left", va = "top", transform = plt.gca().transAxes)
        plt.title("Polygon Visualization")
        plt.legend()
        plt.grid(True)
        plt.gca().set_axisbelow(True)
        plt.show()
    
    def display_result(self):
        print("Points of Polygon:")
        for i, point in enumerate(self.points):
            print(f"{i+1}. point: {point}")
        print(f"\nArea of the polygon: {self.area:.2f} square units")
    
    def main_app(self):
        self.calculate_area()
        self.display_result()
        self.visualize()


def main():
    try:
        length = int(input("Enter number of vertices of polygon: "))
        if length < 3:
            raise ValueError("Polygon must have at least 3 vertices.")
        
        points = []
        for i in range(length):
            x = int(input(f"Enter {i+1}. vertex x coordinate: "))
            y = int(input(f"Enter {i+1}. vertex y coordinate: "))
            points.append(Point(x, y))
        
        app = ShoelaceTheorem(points=points)
        app.main_app()
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
