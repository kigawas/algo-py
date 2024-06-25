"""
https://leetcode.com/problems/trapping-rain-water/
"""


def solve(heights):
    # monotonic stack
    mono = []
    ans = 0
    for i, h in enumerate(heights):
        while mono and mono[-1][1] < h:
            prev_i, prev_h = mono.pop()
            if mono:
                w = i - mono[-1][0] - 1
                ans += w * (min(h, mono[-1][1]) - prev_h)
        mono.append((i, h))
    return ans
