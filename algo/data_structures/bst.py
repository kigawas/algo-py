from __future__ import annotations

from abc import ABC
from typing import Optional


class AbstractNode(ABC):
    @property
    def left(self):
        raise NotImplementedError

    @property
    def right(self):
        raise NotImplementedError

    @property
    def value(self):
        raise NotImplementedError


def height(root: Optional[AbstractNode]) -> int:
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def find(root: Optional[AbstractNode], value: int) -> Optional[AbstractNode]:
    if root is None:
        return None

    if root.value == value:
        return root
    elif root.value < value:
        return find(root.right, value)
    else:
        return find(root.left, value)


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
