from abc import ABC
from abc import abstractmethod
from collections import deque
from dataclasses import dataclass
from dataclasses import field
from heapq import heappop
from heapq import heappush
from typing import Collection
from typing import Deque
from typing import Generic
from typing import List
from typing import TypeVar

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


class PriorityQueue(Bag, Generic[T]):  # min heap
    _bag: List[T] = []

    def push(self, v):
        heappush(self._bag, v)
        return self

    def pop(self):
        return heappop(self._bag)
