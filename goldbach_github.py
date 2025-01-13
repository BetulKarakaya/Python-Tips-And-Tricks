import math
from itertools import combinations

def is_prime(num):
    """
    Checks if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_decomposition(even_number):
    """
    Finds two prime numbers that add up to the given even number.
    """
    if even_number <= 2 or even_number % 2 != 0:
        return "Input must be an even number greater than 2."
    
    # Generate all prime numbers less than the even number
    primes = [num for num in range(2, even_number) if is_prime(num)]
    
    # Find two primes that sum to the even number
    for prime1, prime2 in combinations(primes, 2):
        if prime1 + prime2 == even_number:
            return f"{even_number} = {prime1} + {prime2}"
    
    return "No decomposition found (unlikely if Goldbach's conjecture holds)."

def main():
    print("Goldbach Conjecture Solver".center(50, "-"))
    
    try:
        even_number = int(input("Enter an even number greater than 2: "))
        result = goldbach_decomposition(even_number)
        print(result)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
