"""
https://leetcode.com/problems/permutations/
"""


def solve(nums):
    n = len(nums)
    used = set()
    res = []

    def bt(ans, k):
        if k == n:
            res.append(ans)
            return
        for num in nums:
            print("num:", num, "@", k)
            if num in used:
                continue
            used.add(num)

            print("entering", ans + [num], used, k)
            bt(ans + [num], k + 1)
            used.remove(num)
            print("exiting", ans + [num], used, k)

    bt([], 0)
    return res
