import math
from collections import Counter

def prime_factorization_with_exponents(n):
    """
    Performs prime factorization of a number and returns the prime factors with their exponents.
    
    Parameters:
    - n (int): The number to be factorized (must be >= 2).
    
    Returns:
    - dict: A dictionary where keys are prime factors, and values are their respective exponents.
    """
    factors = []
    original = n
    
    # Handle the factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    # Count the occurrences of each factor
    factor_count = dict(Counter(factors))
    print(f"Prime factorization of {original} is: {factor_count}")
    return factor_count


def main():
    print("Prime Factorization with Exponents".center(60, "="))
    number = int(input("Enter a number (>= 2): "))
    
    if number < 2:
        print("The number must be greater than or equal to 2.")
    else:
        result = prime_factorization_with_exponents(number)
        print("Prime factors with exponents:")
        for factor, exponent in result.items():
            print(f"{factor}^{exponent}")
    print("=" * 60)

if __name__ == "__main__":
    main()
