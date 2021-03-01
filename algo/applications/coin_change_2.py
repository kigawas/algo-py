"""
https://leetcode.com/problems/coin-change-2/
"""


def solve(coins, amount: int) -> int:
    """
    Unbounded knapsack DP. Note the base case is:
    For 0 amount we pick 0 coins, so we have only one way to pick, dp[0] = 1.
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] += dp[t - coin]

    return dp[amount]
