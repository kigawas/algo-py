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
            if num in used:
                continue
            used.add(num)

            bt(ans + [num], k + 1)
            used.remove(num)

    bt([], 0)
    return res
