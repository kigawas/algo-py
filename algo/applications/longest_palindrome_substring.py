"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


def solve(s: str):
    n = len(s)

    def check(i, j):
        # check [i, j), left closed right open range
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
        return i + 1, j

    maxi = 0
    maxj = 1
    for i in range(n - 1):
        i1, j1 = check(i, i)
        i2, j2 = check(i, i + 1)
        if j1 - i1 > maxj - maxi:
            maxj = j1
            maxi = i1
        if j2 - i2 > maxj - maxi:
            maxj = j2
            maxi = i2
    return s[maxi:maxj]
