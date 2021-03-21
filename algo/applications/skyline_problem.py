"""
https://leetcode.com/problems/the-skyline-problem/
"""

from algo.data_structures.fenwick import lowbit


def solve(buildings):
    """
    Binary indexed tree
    """
    res = []

    # preprocess
    points = []
    ends = {}
    for i, (left, right, height) in enumerate(buildings):
        pl = (left, False, height)
        pr = (right, True, height)
        points.extend([pl, pr])
        ends[pl] = pr

    points.sort()

    idx = {points[i]: i for i in range(len(points))}
    bit = [0] * (len(points) + 1)

    def add(i, h):
        # update max h from i to 1
        while i > 0:
            bit[i] = max(bit[i], h)
            i -= lowbit(i)

    def ask(i):
        # get max h from i to n
        res = 0
        while i < len(bit):
            res = max(res, bit[i])
            i += lowbit(i)
        return res

    for i, p in enumerate(points):
        if not p[1]:  # not end, we add h
            end = ends[p]
            add(idx[end], p[2])

        # max h from i+1 to n
        h = ask(i + 1)
        if not res:
            res.append([p[0], h])
        elif res[-1][1] != h:  # current max h is different from previous
            if res[-1][0] == p[0]:
                # same x coord, update h
                res[-1][1] = h
            else:
                res.append([p[0], h])

    return res
