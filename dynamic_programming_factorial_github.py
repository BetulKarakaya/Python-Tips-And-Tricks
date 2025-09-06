class FactorialDP:
    def __init__(self):
        # Memoization table (dynamic programming)
        self.memo = {0: 1, 1: 1}  

    def factorial(self, n: int) -> int:
        """
        Compute factorial using dynamic programming (memoization).
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        if n not in self.memo:
            # Store the result dynamically in memo table
            self.memo[n] = n * self.factorial(n - 1)
        return self.memo[n]


def main():
    dp = FactorialDP()
    
    print("5! =", dp.factorial(5))
    print("20! =", dp.factorial(20))
    print("100! =", dp.factorial(100))

    # Same calls are faster because of memoization
    print("Reusing memoized values:")
    print("5! again =", dp.factorial(5))
    print("100! again =", dp.factorial(100))


if __name__ == "__main__":
    main()
