"""
https://leetcode.com/problems/word-break-ii/
"""

from functools import lru_cache


def solve(s: str, word_list: list[str]):
    n = len(s)
    res = []

    words = set(word_list)
    chars = set("".join(words))
    for c in s:
        if c not in chars:
            return []

    @lru_cache(maxsize=None)
    def valid(w):
        if w not in words:
            return False

        for c in w:
            if c not in chars:
                return False

        return True

    def bt(ans, i):
        if i == n:
            res.append(" ".join(ans))
            return

        for j in range(n, i, -1):
            word = s[i:j]
            if valid(word):
                bt(ans + [word], j)

    bt([], 0)
    return res
