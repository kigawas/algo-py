from random import randint

from .sort import partition


def select_kth_smallest(array: list[int], k: int) -> int:
    assert 0 <= k < len(array)

    pivot_index = randint(0, len(array) - 1)
    rank = partition(array, 0, len(array), pivot_index)  # 0 <= rank < len(array)
    if rank == k:
        return array[rank]
    elif rank < k:
        return select_kth_smallest(array[rank:], k - rank)
    else:
        # rank > k
        return select_kth_smallest(array[:rank], k)
