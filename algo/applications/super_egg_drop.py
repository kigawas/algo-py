"""
Leetcode problem: https://leetcode.com/problems/super-egg-drop/
"""


def solve_dp(K: int, N: int):
    def solve(k, moves):
        dp = [None] * (k + 1)
        for i in range(k + 1):
            dp[i] = [0] * (moves + 1)

        for i in range(1, k + 1):
            for j in range(1, moves + 1):
                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i][j - 1]
        # triangular numbers in DP
        return dp[k][moves]
        # if k == 1:
        #     return moves
        # if moves == 1 or moves == 0:
        #     return moves
        # return 1 + solve(k - 1, moves - 1) + solve(k, moves - 1)

    left, right = 1, N + 1
    while left < right:
        # logN * K * (N/2 + N/4 + ..) ~= K * N * logN
        mid = (left + right) // 2
        if solve(K, mid) >= N:
            # try finding less moves
            right = mid
        else:
            left = mid + 1
    return left
