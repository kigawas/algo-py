from random import randint
from typing import List


def partition(array: List[int], pivot_index: int) -> int:
    # pivot_index = randint(0, len(array) - 1)
    array[-1], array[pivot_index] = array[pivot_index], array[-1]
    # pivot = array[-1]
    i, j = 0, len(array) - 2
    p = array[-1]
    while i < j:
        # invariant:
        # a in array[:i] <= p, a in array[j+1:-1] >= p, array[-1] == p
        # a in array[i:j+1] ? p
        if array[i] <= p:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1

        if array[j] >= p:
            j -= 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1

    if i == j and array[i] < p:
        i += 1

    assert i == j or i == j + 1

    array[-1], array[i] = array[i], array[-1]
    # array[i:-1] >= p, array[:i] <= p
    return i


def select_kth_smallest(array: List[int], k: int) -> int:
    assert 0 <= k < len(array)

    pivot_index = randint(0, len(array) - 1)
    rank = partition(array, pivot_index)  # 0 <= rank < len(array)
    if rank == k:
        return array[rank]
    elif rank < k:
        return select_kth_smallest(array[rank:], k - rank)
    else:
        # rank > k
        return select_kth_smallest(array[:rank], k)
