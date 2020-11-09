from random import shuffle

from algo.algorithms.array.sort import quick_sort


def test_qs():
    a = list(range(0, 1000))
    shuffle(a)
    assert (quick_sort(a)) == sorted(a)
