from random import shuffle

from algo.algorithms.array.select import select_kth_smallest
from algo.algorithms.array.sort import merge_sort, partition, quick_sort

N = 100
LIST = list(range(N))


def check_partition(array, pivot_index):
    p = array[pivot_index]
    r = partition(array, 0, len(array), pivot_index)
    for i in array[:r]:
        assert i <= p

    for i in array[r:]:
        assert i >= p


def check_sort(arr):
    shuffle(arr)
    assert quick_sort(arr) == sorted(arr)

    shuffle(arr)
    assert merge_sort(arr) == sorted(arr)


def test_sort():
    for i in range(N):
        shuffle(LIST)
        check_partition(LIST, i)

    check_sort(LIST)


def test_select():
    for i in range(N):
        shuffle(LIST)
        assert select_kth_smallest(LIST, i) == i
