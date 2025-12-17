# lis_dynamic_programming.py

class LISAnalyzer:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def find_lis_length(self) -> int:
        """
        Dynamic Programming approach to find
        the length of the Longest Increasing Subsequence.
        """
        if not self.numbers:
            return 0

        n = len(self.numbers)
        dp = [1] * n  # dp[i] = LIS ending at index i

        for i in range(n):
            for j in range(i):
                if self.numbers[j] < self.numbers[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        print("DP table:", dp)
        return max(dp)


def main():
    numbers = [10, 9, 2, 5, 3, 7, 101, 18]

    analyzer = LISAnalyzer(numbers)
    lis_length = analyzer.find_lis_length()

    print("\nNumbers:", numbers)
    print("Longest Increasing Subsequence Length:", lis_length)


if __name__ == "__main__":
    main()
