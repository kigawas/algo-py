"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""
from functools import lru_cache


def solve_bt(nums) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False

    n = len(nums)

    @lru_cache(maxsize=None)
    def bt(i, target):
        if i == n:
            return target == 0

        if bt(i + 1, target):
            return True
        elif target >= nums[i] and bt(i + 1, target - nums[i]):
            return True
        return False

    return bt(0, s // 2)


def solve_dp_naive(nums) -> bool:
    """
    0-1 Knapsack DP.

    A simple optimization is to use two rolling arrays and iterate like:
    `dp[i&1][t] = dp[(i - 1)&1][t] or dp[(i - 1)&1][t - nums[i - 1]]`
    """
    s = sum(nums)
    if s % 2 != 0:
        return False

    n = len(nums)
    target = s // 2

    dp = []
    for _ in range(n):
        dp.append([False] * (target + 1))

    dp[0][0] = True
    for i in range(1, n):
        for t in range(target + 1):
            if t >= nums[i - 1]:
                dp[i][t] = dp[i - 1][t] or dp[i - 1][t - nums[i - 1]]
            else:
                dp[i][t] = dp[i - 1][t]

    return dp[n - 1][target]


def solve_dp(nums) -> bool:
    s = sum(nums)
    if s % 2 != 0:
        return False

    n = len(nums)
    target = s // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(1, n):
        for t in range(target, nums[i - 1] - 1, -1):  # reverse!
            dp[t] = dp[t] or dp[t - nums[i - 1]]

    return dp[target]
