"""
https://onlinejudge.u-aizu.ac.jp/courses/library/7/DPL/1/DPL_1_G
"""

from collections import deque


def solve_naive(weights, values, counts, W):
    """
    Reduction to 0-1 knapsack
    """
    dp = [0] * (W + 1)
    for w, v, c in zip(weights, values, counts):
        for _ in range(c):
            for t in range(W, w - 1, -1):  # no k*w and k*v!
                dp[t] = max(dp[t], dp[t - w] + v)
    return max(dp)


def solve_binary(weights, values, counts, W):
    """
    Reduction to 0-1 knapsack with binary combinations
    """
    dp = [0] * (W + 1)

    def split_binary(count):
        s = 0
        k = 1
        while s + k < count:
            yield k
            s += k
            k *= 2
        yield count - s

    for w, v, c in zip(weights, values, counts):
        for k in split_binary(c):
            for t in range(W, k * w - 1, -1):
                dp[t] = max(dp[t], dp[t - k * w] + k * v)

    return max(dp)


def solve_monotonic(weights, values, counts, W):
    """
    With monotonic queue
    """
    dp = [0] * (W + 1)

    def calc(k):
        return dp[u + k * w] - k * v

    for w, v, c in zip(weights, values, counts):
        mono = deque()
        for u in range(w):  # remainders of W / w
            maxp = (W - u) // w
            for k in range(maxp - 1, max(0, maxp - c) - 1, -1):
                while mono and calc(mono[-1]) <= calc(k):
                    mono.pop()
                mono.append(k)
            for p in range(maxp, -1, -1):
                while mono and mono[0] > p - 1:
                    mono.popleft()
                if mono:
                    dp[u + p * w] = max(dp[u + p * w], calc(mono[0]) + p * v)
                if p - c - 1 >= 0:
                    while mono and calc(mono[-1]) <= calc(p - c - 1):
                        mono.pop()
                    mono.append(p - c - 1)
    return max(dp)
