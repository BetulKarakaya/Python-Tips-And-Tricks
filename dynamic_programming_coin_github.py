class CoinChangeSolver:
    def __init__(self, denominations):
        # Available coin/bill denominations
        self.denominations = sorted(denominations, reverse=True)  

    def min_coins_with_combination(self, target_amount):
        """
        Dynamic Programming solution to find 
        the minimum number of coins/bills to make up a given amount.
        Also reconstructs which coins are used.
        """
        # DP array initialized with "infinity"
        dp = [float("inf")] * (target_amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # To reconstruct which coin was used
        prev_coin = [-1] * (target_amount + 1)

        for coin in self.denominations:
            for x in range(coin, target_amount + 1):
                if dp[x - coin] + 1 < dp[x]:
                    dp[x] = dp[x - coin] + 1
                    prev_coin[x] = coin

        if dp[target_amount] == float("inf"):
            return -1, []

        # Reconstruct combination
        combination = []
        amount = target_amount
        while amount > 0 and prev_coin[amount] != -1:
            combination.append(prev_coin[amount])
            amount -= prev_coin[amount]

        return dp[target_amount], combination


def main():
    # Example: Available coins/bills in TL
    denominations = [1, 5, 10, 20]
    target_amount = 133

    solver = CoinChangeSolver(denominations)
    count, combo = solver.min_coins_with_combination(target_amount)

    if count != -1:
        combo_str = " + ".join(f"{c} TL" for c in combo)
        print(f"Minimum coins/bills needed for {target_amount} TL: {count}")
        print(f"Combination: {combo_str} = {target_amount} TL")
    else:
        print(f"Cannot make {target_amount} TL with given denominations.")


if __name__ == "__main__":
    main()
