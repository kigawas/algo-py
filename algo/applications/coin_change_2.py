"""
https://leetcode.com/problems/coin-change-2/
"""


def solve(coins, amount: int) -> int:
    """
    Unbounded knapsack DP. Note the base case is:
    For 0 amount we pick 0 coins, so we have only one way to pick, dp[0] = 1.
    """
    n = len(coins)

    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for t in range(coins[i - 1], amount + 1):
            dp[t] += dp[t - coins[i - 1]]

    return dp[amount]
