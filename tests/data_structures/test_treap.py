import math
import random

from algo.data_structures.bst import find, findmax, findmin, height
from algo.data_structures.treap import Node, delete, insert, merge, split


def test_split_merge():
    n1 = Node(value=3)
    n2 = Node(value=2)
    n3 = Node(value=1)

    n1.left = n2
    n2.left = n3

    left, right = split(n1, 2)
    assert left is n2 and right is n1
    assert left.left is n3

    new_root = merge(left, right)
    assert new_root is n1
    assert find(n1, 2) is n2
    assert find(n1, -1) is None


def test_insert_and_delete():
    N = 1000
    arr = list(range(0, N))
    random.shuffle(arr)

    root = None
    count = 0
    k = 4

    for i in arr:
        priority = random.randint(-N, N)
        root = insert(root, i, priority)
        max_h = int(math.log2(i + 1))
        if max_h * k < height(root):
            count += 1

    assert count < N // 10
    assert findmin(root).value == 0
    assert findmax(root).value == N - 1

    for i in arr:
        find(root, i).value == i

    for i in arr[: N // 2]:
        root = delete(root, i)

    for i in arr[: N // 2]:
        find(root, i) is None

    for i in arr[N // 2 :]:
        find(root, i).value == i
