"""
https://leetcode.com/problems/maximum-subarray/
"""


def solve_dc(nums):
    # divide and conquer
    n = len(nums)

    def dc(i, j):
        # [i, j), 0 <= i <= j < n
        mid = (i + j) // 2
        if i == j:
            return nums[i]
        left = dc(i, mid)
        right = dc(mid + 1, j)

        middle = 0
        midl, midr = mid, mid + 1
        maxl = nums[midl]
        while midl >= i:
            middle += nums[midl]
            maxl = max(maxl, middle)
            midl -= 1

        middle = 0
        maxr = nums[midr]
        while midr <= j:
            middle += nums[midr]
            maxr = max(maxr, middle)
            midr += 1
        middle_max = max(maxl, maxr, maxl + maxr)
        return max(left, right, middle_max)

    return dc(0, n - 1)


def solve_dp(nums):
    n = len(nums)
    dp = [0] * n
    for i, n in enumerate(nums):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
    return max(dp)
