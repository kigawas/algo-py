from random import shuffle

from algo.algorithms.array.sort import merge
from algo.algorithms.array.sort import merge_sort
from algo.algorithms.array.sort import quick_sort


def test_qs():
    a = list(range(0, 1000))
    shuffle(a)
    assert quick_sort(a) == sorted(a)


def test_ms():
    merge([1, 3, 4, 5], [0, 2, 6]) == sorted(list(range(0, 7)))
    a = list(range(0, 1000))
    shuffle(a)
    assert merge_sort(a) == sorted(a)
