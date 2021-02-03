from algo.data_structures.avl import rebalance
from algo.data_structures.bst import is_balanced, is_bst

from .test_bst import get_balance_tree, get_imbalanced_tree, print_tree


def test_balance():
    root = get_imbalanced_tree()
    print_tree(root)

    assert is_bst(root)
    assert not is_balanced(root)

    root = rebalance(root)
    print_tree(root)
    root = rebalance(root)
    print_tree(root)
    assert is_balanced(root)

    print("root")
    print_tree(root)
    print("left")
    print_tree(root.left)
    print("right")
    print_tree(root.right)

    root = get_balance_tree()

    assert is_bst(root)
    assert is_balanced(root)
