class EditDistance:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    def calculate(self) -> int:
        m, n = len(self.word1), len(self.word2)

        # DP table initialization
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i   # delete all characters
        for j in range(n + 1):
            dp[0][j] = j   # insert all characters

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.word1[i - 1] == self.word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],     # delete
                        dp[i][j - 1],     # insert
                        dp[i - 1][j - 1]  # replace
                    )

        print("DP Table:")
        for row in dp:
            print(row)

        return dp[m][n]


def main():
    ed = EditDistance("kitten", "sitting")
    distance = ed.calculate()

    print("\nEdit Distance:", distance)


if __name__ == "__main__":
    main()
