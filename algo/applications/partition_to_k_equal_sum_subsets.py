"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""


def solve(nums, k) -> bool:
    # N.B.: need to find k times
    s = sum(nums)
    if s % k != 0:
        return False

    def bt(i, target, times):
        if times == 0:
            return True
        elif target == 0:
            return bt(n, s // k, times - 1)

        for j in range(i):
            if not used[j] and target >= nums[j]:
                used[j] = True
                if bt(j, target - nums[j], times):
                    return True
                used[j] = False
        return False

    n = len(nums)
    used = [False] * n
    return bt(n, s // k, k)
