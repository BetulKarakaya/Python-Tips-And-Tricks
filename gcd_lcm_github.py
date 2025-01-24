import math

def calculate_gcd(a, b):
    """
    Calculate GCD (Greatest Common Divisor) of two numbers.
    :param a: First number
    :param b: Second number
    :return: GCD
    """
    gcd = math.gcd(a, b)  
    return gcd


def calculate_lcm(a,b,gcd):
    """
    Calculate LCM (Least Common Multiple) of two numbers.
    :param a: First number
    :param b: Second number
    :return: LCM
    """
    lcm = abs(a * b) // gcd  # LCM = |a * b| / GCD
    return lcm


def main():
    
    print("GCD and LCM Calculator".center(50, "-"))
    
    try:
        
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 <= 0 or num2 <= 0:
            raise ValueError("Numbers must be positive integers.")

        # Calculate GCD and LCM
        gcd = calculate_gcd(num1, num2)
        lcm = calculate_lcm(num1, num2, gcd)

       
        print(f"\nThe GCD (EBOB) of {num1} and {num2} is: {gcd}")
        print(f"The LCM (EKOK) of {num1} and {num2} is: {lcm}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()