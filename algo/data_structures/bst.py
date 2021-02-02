from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Callable, Optional


class AbstractNode(ABC):
    @property
    def left(self) -> Optional[AbstractNode]:
        raise NotImplementedError

    @left.setter
    def left(self):
        raise NotImplementedError

    @property
    def right(self) -> Optional[AbstractNode]:
        raise NotImplementedError

    @right.setter
    def right(self):
        raise NotImplementedError

    @property
    def value(self):
        raise NotImplementedError


@dataclass
class Node(AbstractNode):
    left: Optional[Node] = None
    right: Optional[Node] = None
    value: int = 0


def visit(
    root: Optional[AbstractNode],
    level: int,
    callback: Callable[[int, int], None],
):
    if root is None:
        return

    callback(root.value, level)
    visit(root.left, level + 1, callback)
    visit(root.right, level + 1, callback)


def height(root: Optional[AbstractNode]) -> int:
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def is_balanced(root: Optional[AbstractNode]) -> bool:
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    return abs(lh - rh) < 2


def find(root: Optional[AbstractNode], value: int) -> Optional[AbstractNode]:
    if root is None:
        return None
    elif root.value == value:
        return root
    elif root.value < value:
        return find(root.right, value)
    else:
        return find(root.left, value)


def find_parent(root: Optional[AbstractNode], value: int) -> Optional[AbstractNode]:
    prev, cur = None, root
    while cur is not None:
        if cur.value == value:
            return prev
        elif cur.value < value:
            prev, cur = cur, cur.right
        else:
            prev, cur = cur, cur.left
    return prev


def findmin(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    if root is None:
        return None

    if root.left is None:
        return root
    return findmin(root.left)


def findmax(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    if root is None:
        return None

    if root.right is None:
        return root
    return findmax(root.right)


def is_bst(root: Optional[AbstractNode]) -> bool:
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        return root.right.value > root.value and is_bst(root.right)
    elif root.right is None and root.left is not None:
        return root.left.value < root.value and is_bst(root.left)

    assert root.left is not None and root.right is not None

    is_valid = root.left.value < root.value < root.right.value
    return is_valid and is_bst(root.left) and is_bst(root.right)


def reverse(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    if root is None:
        return None

    root.left, root.right = reverse(root.right), reverse(root.left)
    return root


def rotate_to_right(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    r"""
    ```
                        y                         x
                      /   \                     /   \
                     /     \                   /     \
                    x       C       ->        A       y
                  /   \                             /   \
                 /     \                           /     \
                A       B                         B       C
    ```
    """
    if root is None:
        return None
    elif root.left is None:
        return root

    x = root.left
    root.left = x.right
    x.right = root
    return x


def rotate_to_left(root: Optional[AbstractNode]) -> Optional[AbstractNode]:
    r"""
    ```
                        y                         x
                      /   \                     /   \
                     /     \                   /     \
                    x       C       <-        A       y
                  /   \                             /   \
                 /     \                           /     \
                A       B                         B       C
    ```
    """
    if root is None:
        return None
    elif root.right is None:
        return root

    y = root.right
    root.right = y.left
    y.left = root
    return y


def rotate_up(root: Optional[AbstractNode], value: int) -> Optional[AbstractNode]:
    # rotate a Node to root
    if root is None:
        return None
    elif root.value == value:
        return root
    elif root.value < value:
        root.right = rotate_up(root.right, value)
        return rotate_to_left(root)
    else:
        root.left = rotate_up(root.left, value)
        return rotate_to_right(root)


def rotate_down(root: Optional[AbstractNode], value: int) -> Optional[AbstractNode]:
    # rotate a Node to leaf
    if root is None:
        return None
    elif root.value == value:
        lh = height(root.left)
        rh = height(root.right)
        if lh < rh:
            return rotate_to_left(root)
        else:
            return rotate_to_right(root)
    elif root.value < value:
        root.right = rotate_down(root.right, value)
        return root
    else:
        root.left = rotate_down(root.left, value)
        return root
