"""
https://leetcode.com/problems/target-sum/
"""
from functools import lru_cache


def solve_bt(nums, S):
    n = len(nums)

    @lru_cache(maxsize=None)
    def solve(i, ans):
        if i > n:
            return 0
        elif i == n:
            if ans == S:
                return 1
            else:
                return 0

        return solve(i + 1, ans + nums[i]) + solve(i + 1, ans - nums[i])

    return solve(0, 0)


def solve_dp(nums, S):
    """
    Let A = sum of numbers with "+" and B = sum of numbers with "-".
    We have A + B = sum(nums), A - B = S.
    So 2A = sum(nums) + S, if sum(nums) + S is not even, no solution;
    otherwise, find target = (sum(nums) + S) // 2
    """
    SN = sum(nums)
    if (SN + S) & 1 == 1 or SN < S or SN < -S:
        return 0

    target = (SN + S) // 2
    dp = [0] * (target + 1)
    dp[0] = 1
    for num in nums:
        for t in range(target, num - 1, -1):  # reverse!
            dp[t] = dp[t] + dp[t - num]

    return dp[target]
