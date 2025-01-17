import math

def is_perfect_square(n):
    
    sqrt_n = int(math.sqrt(n))  # Calculate the integer part of the square root of n
    return sqrt_n * sqrt_n == n # Check if squaring this integer gives back the original number

def digit_square_check(number):
   
    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(number))
    digit_square = digit_sum ** 2

    # Check if the square is a perfect square
    if is_perfect_square(digit_square):
        return f"The square of the sum of digits ({digit_sum}² = {digit_square}) is a perfect square!"
    else:
        return f"The square of the sum of digits ({digit_sum}² = {digit_square}) is NOT a perfect square."

def main():
    
    print("Welcome to the Digit Square Checker!")
    number = int(input("Enter a positive integer: "))
    print(digit_square_check(number))

if __name__ == "__main__":
    main()
