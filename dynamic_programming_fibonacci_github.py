class FibonacciDP:
    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def fibonacci_top_down(self, n: int) -> int:
        """
        Recursive + Memoization (Top-Down DP)
        """
        if n not in self.memo:
            self.memo[n] = self.fibonacci_top_down(n - 1) + self.fibonacci_top_down(n - 2)
        return self.memo[n]

    def fibonacci_bottom_up(self, n: int) -> int:
        """
        Iterative (Bottom-Up DP)
        """
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


def main():
    fib = FibonacciDP()

    n = 100
    print(f"Top-Down Fibonacci({n}) =", fib.fibonacci_top_down(n))
    print(f"Bottom-Up Fibonacci({n}) =", fib.fibonacci_bottom_up(n))


if __name__ == "__main__":
    main()
