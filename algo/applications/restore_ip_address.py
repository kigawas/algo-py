"""
https://leetcode.com/problems/restore-ip-addresses/
"""


def solve(s):
    res = []
    n = len(s)
    if n > 12:
        return []

    def bt(ans, i):
        if i == n and len(ans) == 4:
            res.append(".".join(ans))
            return
        for j in range(i + 1, n + 1):
            if len(ans) < 4:
                candidate = s[i:j]
                v = int(candidate)
                if v <= 255 and str(v) == candidate:
                    bt(ans + [candidate], j)

    bt([], 0)
    return res
