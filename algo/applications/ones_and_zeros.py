"""
https://leetcode.com/problems/ones-and-zeroes/
"""


def solve(strs, m, n):
    """
    2D 0-1 knapsack
    """

    def count(s):
        m, n = 0, 0
        for c in s:
            if c == "0":
                m += 1
            elif c == "1":
                n += 1
        return m, n

    dp = []
    for _ in range(m + 1):
        dp.append([0] * (n + 1))

    for s in strs:
        mi, ni = count(s)
        for j in range(m, mi - 1, -1):  # reverse!
            for k in range(n, ni - 1, -1):  # reverse!
                dp[j][k] = max(dp[j][k], dp[j - mi][k - ni] + 1)
    return dp[m][n]
