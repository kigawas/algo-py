from typing import Optional

from .bst import AbstractNode
from .bst import height
from .bst import rotate_to_left
from .bst import rotate_to_right


def rebalance(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    # AVL
    if root is None:
        return None

    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) < 2:
        # do nothing
        return root
    elif lh > rh:
        assert root.left is not None
        if height(root.left.left) < height(root.left.right):
            rotate_to_left(root.left)

        return rotate_to_right(root)
    else:
        assert root.right is not None
        if height(root.right.left) > height(root.right.right):
            rotate_to_right(root.right)

        return rotate_to_left(root)
