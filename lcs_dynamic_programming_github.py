def lcs(text1: str, text2: str) -> tuple[int, str]:
    n, m = len(text1), len(text2)

    # 1) DP TABLE
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 2) BACKTRACKING (sequence reconstruction)
    i, j = n, m
    sequence = []

    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            sequence.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    sequence.reverse()
    return dp[n][m], "".join(sequence)


def main():
    a = "ABCBDABABBN"
    b = "BABABBD"

    length, subseq = lcs(a, b)

    print(f"LCS Length: {length}")
    print(f"LCS Sequence: {subseq}")


if __name__ == "__main__":
    main()
