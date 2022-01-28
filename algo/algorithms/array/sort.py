from random import randint


def partition(A: list[int], left: int, right: int, pivot_index: int):
    A[pivot_index], A[left] = A[left], A[pivot_index]
    pivot = A[left]

    i, j = left + 1, right
    # use [left, right) to make sure i == j before return
    while i < j:
        # invariant:
        # A[left:i] <= p, A[j-1:right] >= p
        # A[i] < A[j-1]
        # A[i:j] ? p

        if A[i] <= pivot:
            i += 1
        if A[j - 1] > pivot:
            j -= 1

        if i < j and A[i] >= A[j - 1]:
            A[i], A[j - 1] = A[j - 1], A[i]

    assert i == j
    A[i - 1], A[left] = A[left], A[i - 1]
    # A[left: i] <= p, A[i: right] >= p
    return i - 1


def quick_sort(A: list[int]) -> list[int]:
    n = len(A)

    def qsort(A, i, j):
        if i >= j:
            return

        q = partition(A, i, j, randint(i, j - 1))
        qsort(A, i, q)
        qsort(A, q + 1, j)

    qsort(A, 0, n)
    return A


def merge(A: list[int], B: list[int]) -> list[int]:
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


def merge_sort(array: list[int]) -> list[int]:
    if len(array) in (0, 1):
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)
