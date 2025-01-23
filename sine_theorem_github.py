import math
import matplotlib.pyplot as plt
import numpy as np

class Triangle:
    def __init__(self, side_a, angle_a, angle_b):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = angle_b
    
    def calculate_side_b(self):
        self.radian_a = math.radians(self.angle_a)
        self.radian_b = math.radians(self.angle_b)

        self.side_b = (self.side_a * math.sin(self.radian_b)) / math.sin(self.radian_a)
    
    def calculate_side_c(self):
        self.angle_c = 180 - (self.angle_a + self.angle_b)
        self.radian_a = math.radians(self.angle_a)
        self.radian_c = math.radians(self.angle_c)

        self.side_c = (self.side_a * math.sin(self.radian_c)) / math.sin(self.radian_a)
    
    def verify_calculation(self):
        if not math.isclose(
            self.side_a / math.sin(self.radian_a),
            self.side_b / math.sin(self.radian_b),
            rel_tol=1e-9
        ) or not math.isclose(
            self.side_b / math.sin(self.radian_b),
            self.side_c / math.sin(self.radian_c),
            rel_tol=1e-9
        ):
            raise ValueError("Triangle verification failed. Sine theorem is not satisfied.")

    def calculate_circumcircle(self):
        
        # Vertices of the triangle
        A = np.array([0, 0])
        B = np.array([self.side_c, 0])
        angle_c_rad = math.radians(self.angle_c)
        C = np.array([
            self.side_b * math.cos(angle_c_rad),
            self.side_b * math.sin(angle_c_rad)
        ])
        self.vertices = (A, B, C)

        # Calculate triangle circumcenter
        D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
        Ux = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) +
              (B[0]**2 + B[1]**2) * (C[1] - A[1]) +
              (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D
        Uy = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) +
              (B[0]**2 + B[1]**2) * (A[0] - C[0]) +
              (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D
        self.circumcenter = np.array([Ux, Uy])

        # Circumcircle radius
        self.circumradius = np.linalg.norm(A - self.circumcenter)

    def plot_triangle_with_circumcircle(self):
        A, B, C = self.vertices

        # Draw triangle
        plt.plot([A[0], B[0]], [A[1], B[1]], 'r', label=f'side a = {self.side_a}')
        plt.plot([B[0], C[0]], [B[1], C[1]], 'g', label=f'side b = {self.side_b:.2f}')
        plt.plot([C[0], A[0]], [C[1], A[1]], 'b', label=f'side c = {self.side_c:.2f}')

        # Draw the circumcircle
        circle = plt.Circle(
            self.circumcenter, self.circumradius, color='purple', fill=False, linestyle='--', label='Circumcircle'
        )
        plt.gca().add_artist(circle)

        # Mark points and center
        plt.scatter(*A, color='black', label='A (0, 0)')
        plt.scatter(*B, color='black', label=f'B ({self.side_c}, 0)')
        plt.scatter(*C, color='black', label=f'C ({C[0]:.2f}, {C[1]:.2f})')
        plt.scatter(*self.circumcenter, color='orange', label='Circumcenter')

        plt.axis('equal')
        plt.legend()
        plt.title("Triangle with Circumcircle")
        plt.show()


def main():
    print("Welcome To Sine Theorem Calculator".center(100, "-"))
    try:
        side_a = int(input("Enter the length of side a: "))
        angle_a = int(input("Enter the degree of the angle showing (directly opposite) side a: "))
        angle_b = int(input("Enter the degree of the angle showing (directly opposite) side b: "))

        # Verify
        if angle_a + angle_b >= 180:
            raise ValueError("The sum of angle_a and angle_b must be less than 180.")

        
        triangle = Triangle(side_a=side_a, angle_a=angle_a, angle_b=angle_b)
        triangle.calculate_side_b()
        triangle.calculate_side_c()
        triangle.verify_calculation()
        triangle.calculate_circumcircle()

        print(f"Side b is {triangle.side_b:.2f}")
        print(f"Side c is {triangle.side_c:.2f}")
        print(f"Angle c is {triangle.angle_c:.2f}")
        print(f"Circumradius is {triangle.circumradius:.2f}")
        print(f"Circumcenter is {triangle.circumcenter}")

        # Draw triangle and circumcircle
        triangle.plot_triangle_with_circumcircle()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
