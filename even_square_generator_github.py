def even_suquares_calculator(range_max):
    # Create a list of squares of even numbers between 1 and range_max(included) using list comprehension
    # List comprehension is a compact way to generate lists in Python.

    # Generating the list
    even_squares = [x**2 for x in range(1, range_max+1) if x % 2 == 0]
    # Explanation of the list comprehension:
    # 1. `x**2`: The operation performed on each element (square of x).
    # 2. `for x in range(1, range_max+1)`: Iterates over numbers from 1 to range_max+1.
    # 3. `if x % 2 == 0`: Filters only even numbers from the range.

    return even_squares

if __name__ == "__main__":
    
    range_max = int(input("Please Enter The Max Value(Included):"))
    # Print the resulting list
    print(f"Squares of even numbers between 1 and {range_max}({range_max} included):", even_suquares_calculator(range_max))
