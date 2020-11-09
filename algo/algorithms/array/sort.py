from random import randint
from typing import List


def quick_sort(array: List[int]) -> List[int]:
    if len(array) in (0, 1):
        return array

    pivot = array[randint(0, len(array) - 1)]

    left = [i for i in array if i < pivot]
    middle = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)
