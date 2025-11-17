import math

class Vector2D:
    """Simple 2D vector class supporting magnitude, dot product, angle, and distance."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def magnitude(self) -> float:
        """Return the vector length."""
        return math.sqrt(self.x**2 + self.y**2)

    def normalized(self):
        """Return a new normalized vector (length 1)."""
        mag = self.magnitude()
        return Vector2D(self.x / mag, self.y / mag)

    def dot(self, other) -> float:
        """Dot product with another vector."""
        return self.x * other.x + self.y * other.y

    def angle_with(self, other) -> float:
        """Return the angle (in degrees) between this vector and another."""
        dot = self.dot(other)
        mags = self.magnitude() * other.magnitude()
        cos_theta = dot / mags
        
        # Numerical safety (bazı ekstrem floating point durumları için)
        cos_theta = max(-1, min(1, cos_theta))

        return math.degrees(math.acos(cos_theta))

    def distance_to(self, other) -> float:
        """Euclidean distance between two vectors."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


def main():
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 0)

    print("V1:", v1)
    print("V2:", v2)

    print("\n- Magnitude of V1:", v1.magnitude())
    print("- Angle between V1:{v1} and V2:{v2}:", v1.angle_with(v2))
    print("- Dot product:", v1.dot(v2))
    print(f"- Distance between V1:{v1} and V2:{v2}:", v1.distance_to(v2))
    print("- Normalized V1:", v1.normalized())


if __name__ == "__main__":
    main()
