from algo.data_structures.bst import find
from algo.data_structures.bst import find_parent
from algo.data_structures.bst import is_balanced
from algo.data_structures.bst import is_bst
from algo.data_structures.bst import Node
from algo.data_structures.bst import reverse
from algo.data_structures.bst import rotate_down
from algo.data_structures.bst import rotate_to_left
from algo.data_structures.bst import rotate_to_right
from algo.data_structures.bst import rotate_up
from algo.data_structures.bst import visit


def get_imbalanced_tree(count: int = 5):
    nodes = []
    for i in range(count):
        nodes.append(Node(value=i + 1))

    prev = nodes[0]
    for n in nodes[1:]:
        prev.right = n
        prev = n

    return nodes[0]


def get_balance_tree():
    n1 = Node(value=1)
    n2 = Node(value=2)
    n3 = Node(value=3)

    n2.left = n1
    n2.right = n3
    return n2


def print_tree(root):
    res = []

    def push(value, level):
        if len(res) == level:
            res.append([])
        res[level].append(value)

    visit(root, 0, push)
    print(res)


def test_node():
    n1 = Node(value=1)
    n2 = Node(value=2)
    n3 = Node(value=3)

    n1.left = n2
    n2.left = n3

    assert not is_bst(n1)
    assert not is_balanced(n1)


def test_reverse():
    n1 = Node(value=1)
    n2 = Node(value=2)
    n3 = Node(value=3)
    n4 = Node(value=4)
    n5 = Node(value=5)
    n3.left = n2
    n2.right = n1
    n3.right = n5
    n5.left = n4
    root = reverse(reverse(n3))
    assert root is n3
    assert root.left is n2
    assert root.right is n5
    assert root.right.left is n4


def test_search():
    root = get_imbalanced_tree()
    assert find(root, 5).value == 5
    assert find(root, 4).value == 4
    assert find_parent(root, 5).value == 4
    assert find_parent(root, 1) is None
    assert find_parent(root, 6).value == 5
    assert find_parent(root, -1).value == 1


def test_rotate():
    root = get_balance_tree()
    assert is_balanced(root)

    rotated_right = rotate_to_right(get_balance_tree())
    assert rotated_right.value == 1
    assert rotated_right.right.value == 2
    assert rotated_right.right.right.value == 3

    rotated_left = rotate_to_left(get_balance_tree())
    assert rotated_left.value == 3
    assert rotated_left.left.value == 2
    assert rotated_left.left.left.value == 1


def test_rotate_up_down():
    root = get_imbalanced_tree()
    root = rotate_up(root, 4)
    assert root.value == 4

    root = get_imbalanced_tree()
    root = rotate_down(root, 3)
    assert root.value == 1
    node = find(root, 3)
    assert node.left is None and node.right is None
