"""
https://leetcode.com/problems/palindrome-partitioning/
"""


def solve(s: str):
    n = len(s)
    res = []

    def backtracking(ans, i):
        if i == n:
            res.append(ans)
            return
        for k in range(i, n):
            sub_s = s[i : k + 1]
            if sub_s == sub_s[::-1]:
                backtracking(ans + (sub_s,), k + 1)

    backtracking(tuple(), 0)
    return res
