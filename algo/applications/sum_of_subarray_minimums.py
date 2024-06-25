from algo.algorithms.array.stack import monotonic

"""
Leetcode problem: https://leetcode.com/problems/sum-of-subarray-minimums/

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""


def solve(A: list[int]) -> int:
    arr = [0] + A + [0]
    res = 0

    def should_pop(index: int, mono: list[int]) -> bool:
        nonlocal res
        cond = arr[mono[-1]] > arr[index]
        if cond:
            # invariant:
            # arr[mono[i]] <= arr[mono[i+1]], arr[mono[-1]] <= arr[index]
            # if violated, we need to clear the mono stack and count minimums
            mono_right = mono[-1]
            mono_left = mono[-2]
            # ----> minimum value * A * B
            res += arr[mono_right] * (index - mono_right) * (mono_right - mono_left)
            # A == count of array containing arr[mono[-1]] as minimum, arr[mono[-1]] is the leftest
            # e.g. 1 in [3, 1, 2, 4]: [1], [1, 2], [1, 2, 4]
            # B == count of array not containing arr[mono[-1]] plus 1, arr[mono[-1]] is the neighbor
            # e.g. 1 in [3, 1, 2, 4]: [3]
            # multiply 3 * (1 + 1): [1], [1, 2], [1, 2, 4], [3, 1], [3, 1, 2], [3, 1, 2, 4]
        return cond

    monotonic(len(arr), should_pop)
    return res % (10**9 + 7)
