from algo.algorithms.array.binary_search import general_lower_bound

"""
Leetcode problem: https://leetcode.com/problems/super-egg-drop/
"""


def solve_by_dp(K: int, N: int):

    from functools import lru_cache

    @lru_cache(maxsize=K * N)
    def dp(K, N):
        if K == 1:
            return N
        if N == 0:
            return 0

        res = float("INF")

        def closure(mid: int) -> bool:
            nonlocal res
            broken = dp(K - 1, mid - 1)
            not_broken = dp(K, N - mid)
            cond = broken <= not_broken
            if cond:
                res = min(res, not_broken + 1)
            else:
                res = min(res, broken + 1)
            return cond

        general_lower_bound(closure, 1, N + 1)
        return res

    res = dp(K, N)
    print(dp.cache_info())
    return res
