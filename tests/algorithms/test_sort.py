from random import shuffle

from algo.algorithms.array.select import partition, select_kth_smallest
from algo.algorithms.array.sort import merge, merge_sort, quick_sort


def test_qs():
    a = list(range(0, 1000))
    shuffle(a)
    assert quick_sort(a) == sorted(a)


def check(array, pivot_index):
    p = array[pivot_index]
    r = partition(array, pivot_index)
    for i in array[:r]:
        assert i <= p

    for i in array[r:]:
        assert i >= p


def test_ms():
    merge([1, 3, 4, 5], [0, 2, 6]) == sorted(list(range(0, 7)))
    a = list(range(0, 1000))
    shuffle(a)
    assert merge_sort(a) == sorted(a)

    for i in range(10):
        b = list(range(10))
        shuffle(b)
        check(b, i)


def test_select():

    for i in range(10):
        b = list(range(10))
        shuffle(b)
        assert select_kth_smallest(b, i) == i
