from __future__ import annotations

from dataclasses import dataclass
from typing import Optional
from typing import Tuple

from .bst import find
from .bst import Node as _Node


@dataclass
class Node(_Node):
    left: Optional[Node] = None
    right: Optional[Node] = None
    priority: int = 0


def split(root: Optional[Node], value: int) -> Tuple[Optional[Node], Optional[Node]]:
    r"""
    Given:
    ```
         R                A                B
       /   \            /   \            /   \
      /     \          /     \          /     \
     A       B       LA       RA      LB       RB
    ```
    If value < R.value, to keep the B subtree, set R.left = RA, return (LA, R):
    ```
         R                             LA                R
       /   \            ->           /    \            /   \
      /     \                       /      \          /     \
     A       B                    ??        ??      RA       B
    ```
    Else, to keep the A subtree, set R.right = LB, return (R, RB):
    ```
         R                             R                RB
       /   \            ->           /   \            /    \
      /     \                       /     \          /      \
     A       B                     A       LB      ??        ??
    ```
    """
    if root is None:
        return None, None

    if value < root.value:
        left, right = split(root.left, value)
        root.left = right
        return left, root
    else:
        left, right = split(root.right, value)
        root.right = left
        return root, right


def merge(root_l: Optional[Node], root_r: Optional[Node]) -> Optional[Node]:
    r"""
    Supposing A.value <= B.value:
    ```
          A                B
        /   \            /   \
       /     \          /     \
     LA       RA      LB       RB
    ```
    If A.priority > B.priority, set A.right = merge(RA, B), return A;
    ```
          A
        /   \
       /     \
     LA                 RA                  B
            merge(     /   \      ,       /   \    )
                      ?     ?            /     \
                                       LB       RB

    ```
    Else, set B.left = merge(A, LB), return B.
    ```
                                     B
                                   /   \
                                  /     \
    merge(    A     ,      LB    )       RB
            /   \         /  \
           /     \       ?    ?
         LA       RA

    ```
    """
    if root_r is None:
        return root_l
    if root_l is None:
        return root_r

    if root_l.value > root_r.value:
        raise ValueError

    if root_l.priority > root_r.priority:  # < is also okay
        root_l.right = merge(root_l.right, root_r)
        return root_l
    else:
        root_r.left = merge(root_l, root_r.left)
        return root_r


def insert(root: Optional[Node], value: int, priority: int = 0) -> Optional[Node]:
    r"""
    Split root to `A` and `B`, which means `value`s in `A` <= `value` and `values` in `B` > `value`
    ```
          A                B
        /   \            /   \
       /     \          /     \
      ?       ?        ?       ?
    ```
    Then merge `A` and a new `Node` to `A'`, if `value` is not found.
    ```
    merge(    A     ,       Node    )  => A'
            /   \          /    \
           /     \       None   None
          ?       ?
    ```
    Finally, merge `A'` and `B`.
    ```
                  A'                  B
    merge(      /   \    ,          /   \    )
               ?     ?             ?     ?
    ```
    """
    left, right = split(root, value)

    if find(root, value) is None:
        left = merge(left, Node(value=value, priority=priority))

    return merge(left, right)


def delete(root: Optional[Node], value: int) -> Optional[Node]:
    left, right = split(root, value - 1)
    node, greater = split(right, value)
    del node
    return merge(left, greater)
