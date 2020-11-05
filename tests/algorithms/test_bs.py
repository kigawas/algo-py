import bisect

from algo.algorithms.array.binary_search import binary_search
from algo.algorithms.array.binary_search import lower_bound
from algo.algorithms.array.binary_search import upper_bound


def test_bs():
    a = [1, 2, 3, 4, 5, 6, 7]

    assert lower_bound(a, -1) == 0
    assert lower_bound(a, 100) == 7

    for t in range(a[0], a[-1] + 1):
        assert bisect.bisect_left(a, t) == lower_bound(a, t) == binary_search(a, t)
        assert bisect.bisect_right(a, t) == upper_bound(a, t) == t

    assert binary_search(a, -1) == -1
    assert binary_search(a, 10) == -1

    a = [1, 1, 1]

    # equal_range(a, t) is [lower_bound(a, t), upper_bound(a, t))
    assert (lower_bound(a, 1), upper_bound(a, 1)) == (0, 3)
    assert (lower_bound(a, 10), upper_bound(a, 10)) == (3, 3)
    assert (lower_bound(a, -1), upper_bound(a, -1)) == (0, 0)
