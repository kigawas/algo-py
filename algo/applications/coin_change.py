"""
https://leetcode.com/problems/coin-change/
"""


def solve_bt(coins, amount: int) -> int:
    INF = 1 << 31
    n = len(coins)
    res = INF
    coins.sort()

    def bt(i, target, count):
        nonlocal res
        if i == n:
            if target == 0:
                res = min(res, count)
                return
            else:
                return
        elif count > res:
            return

        # not pick i, move
        bt(i + 1, target, count)

        if target >= coins[i]:
            # pick i, not move
            bt(i, target - coins[i], count + 1)

    bt(0, amount, 0)
    return res if res != INF else -1


def solve_dp_naive(coins, amount: int) -> int:
    """
    Unbounded knapsack DP.
    Note that we use n+1 instead of n rows as 0-1 knapsack to simplify.
    Row 0 means we **don't** consider any coin, row i>0 means we consider `coins[i-1]`.

    If you really want to use n rows, you can handle row 0 like this before entering the main loop:
    ```python
    for t in range(1, amount + 1):
        if t >= coins[0]:
            dp[0][t] = dp[0][t - coins[0]] + 1
    ```
    """
    INF = 1 << 31
    n = len(coins)
    dp = []
    for i in range(n + 1):
        dp.append([INF] * (amount + 1))
        dp[i][0] = 0

    for i in range(1, n + 1):
        for t in range(1, amount + 1):
            if t >= coins[i - 1]:
                dp[i][t] = min(dp[i - 1][t], dp[i][t - coins[i - 1]] + 1)
            else:
                dp[i][t] = dp[i - 1][t]
    return dp[n][amount] if dp[n][amount] < INF else -1


def solve_dp(coins, amount: int) -> int:
    INF = 1 << 31
    n = len(coins)

    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for t in range(coins[i - 1], amount + 1):  # not like 0-1 knapsack, no reverse!
            dp[t] = min(dp[t], dp[t - coins[i - 1]] + 1)

    return dp[amount] if dp[amount] < INF else -1
