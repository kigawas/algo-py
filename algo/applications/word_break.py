"""
https://leetcode.com/problems/word-break/
"""
from functools import lru_cache


def solve(s: str, word_list: list[str]):
    n = len(s)

    words = set(word_list)
    chars = set("".join(words))
    for c in s:
        if c not in chars:
            return False

    @lru_cache(maxsize=None)
    def dp(i, j):
        # [i, j)
        if i >= j:
            return False
        elif s[i:j] in words:
            return True
        for k in range(i + 1, j):
            if dp(i, k) and dp(k, j):
                return True
        return False

    return dp(0, n)
