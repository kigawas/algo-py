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


def merge(A: List[int], B: List[int]) -> List[int]:
    i, j = 0, 0

    res = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1

    if j == len(B):
        # a in A[i:] >= b in B
        res.extend(A[i:])
    elif i == len(A):
        # b in B[j:] >= a in A
        res.extend(B[j:])

    return res


def merge_sort(array: List[int]) -> List[int]:
    if len(array) in (0, 1):
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)
