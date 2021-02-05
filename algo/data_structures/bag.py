from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field
from heapq import heapify, heappop, heappush
from typing import Collection, Deque, Generic, List, Optional, Tuple, TypeVar

T = TypeVar("T")


class Bag(ABC):
    _bag: Collection

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def push(self, v):
        raise NotImplementedError

    def is_empty(self):
        return len(self._bag) == 0


@dataclass
class Stack(Bag):
    _bag: List = field(default_factory=list)

    def push(self, v):
        self._bag.append(v)
        return self

    def pop(self):
        return self._bag.pop()


class Queue(Bag):
    _bag: Deque = deque([])

    def push(self, v):
        self._bag.append(v)
        return self

    def pop(self):
        return self._bag.popleft()


class PriorityQueue(Bag, Generic[T]):  # min binary heap
    _bag: List[Tuple[int, T]] = []

    def push(self, item, priority=0):
        heappush(self._bag, (priority, item))
        return self

    def pop(self):
        p, item = heappop(self._bag)
        return item, p

    def decrease_key(self, item, priority):
        index = self._find(item)
        if index is None:
            raise ValueError("item not found")

        self._bag[index] = (priority, item)
        heapify(self._bag)

    def _find(self, item) -> Optional[int]:
        i = 0

        while i < len(self._bag):
            if self._bag[i][1] == item:
                return i
            elif self._bag[i + 1][1] == item:
                return i + 1
            i = i * 2 + 1

        return None
