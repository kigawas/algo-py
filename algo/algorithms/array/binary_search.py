from typing import Callable


def general_lower_bound(is_upper_valid: Callable[[int], bool], left: int, right: int):
    """
    General lower bound framework
    """

    while left < right:
        mid = (left + right) // 2
        if is_upper_valid(mid):
            left = mid + 1
        else:
            right = mid

    return left


def lower_bound(array: list[int], target: int, *, left: int = 0, right: int = None):
    """
    Search i for array[i] >= target and array[j] < target, i in [left, right) and j in [0, left).
    Does not exist if i == right
    """

    if right is None:
        right = len(array)

    return general_lower_bound(lambda mid: array[mid] < target, left, right)


def upper_bound(array: list[int], target: int, *, left: int = 0, right: int = None):
    """
    Search i for array[i] > target and array[j] <= target, i in [left, right) and j in [0, left).
    Does not exist if i == right
    """
    if right is None:
        right = len(array)

    # array[mid] <= target
    # see https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L32
    return general_lower_bound(lambda mid: not (target < array[mid]), left, right)


def binary_search(array: list[int], target: int, *, left: int = 0, right: int = None):
    """
    Perform binary search in array[i] for i in [left, right).
    Does not exist if i == -1
    """
    if right is None:
        right = len(array)

    lb = lower_bound(array, target, left=left, right=right)
    if lb == right:
        return -1
    elif array[lb] == target:
        return lb
    else:
        return -1
