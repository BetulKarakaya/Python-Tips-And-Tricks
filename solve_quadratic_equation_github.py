import math

def solve_quadratic_equation(a, b, c):
    """
    Solves a quadratic equation of the form ax² + bx + c = 0.
    Uses the math module for calculations.

    Parameters:
    - a (float): Coefficient of x².
    - b (float): Coefficient of x.
    - c (float): Constant term.

    Returns:
    - A string describing the roots of the equation or a message if no real roots exist.
    """
    try:
        # Calculate discriminant (Delta): b^2 - 4ac
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            # Two distinct real roots (using the quadratic formula)
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)  # First root
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Second root
            return f"The roots are real and distinct: {root1:.2f} and {root2:.2f}"
        elif discriminant == 0:
            # One real root (roots are equal)
            root = -b / (2 * a)  # Single root
            return f"The roots are real and equal: {root:.2f}"
        else:
            # Discriminant < 0: No real roots
            return "The equation has no real roots."
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function to take user input and solve the quadratic equation.
    """
    print("Quadratic Equation Solver (ax² + bx + c = 0)")

    try:
        # Get input values for coefficients a, b, and c
        a = float(input("Enter the coefficient a (for x²): "))
        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return

        b = float(input("Enter the coefficient b (for x): "))
        c = float(input("Enter the constant term c: "))

        # Solve the equation and display the result
        result = solve_quadratic_equation(a, b, c)
        print(result)

    except ValueError:
        print("Invalid input. Please enter numeric values for a, b, and c.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()