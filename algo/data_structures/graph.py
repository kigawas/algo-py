from __future__ import annotations

from collections.abc import Mapping
from typing import Callable, Dict, Iterator, Optional, Set, TypeVar

from .bag import Bag

T = TypeVar("T")
ScoreT = TypeVar("ScoreT", int, float)


class Graph(Mapping[T, Dict[T, int]]):
    def __init__(self) -> None:
        self._g: Dict[T, Dict[T, int]] = {}
        self._vertices: Set[T] = set()

    @property
    def g(self):
        return self._g

    def __len__(self) -> int:
        return len(self._g)

    def __getitem__(self, u: T) -> Dict[T, int]:
        return self._g.get(u, {})

    def __iter__(self) -> Iterator[T]:
        for u in self._g:
            yield u

    @classmethod
    def from_dict(cls, d: Dict[T, Dict[T, int]]) -> Graph:
        g = cls()
        for u, adj in d.items():
            for v, weight in adj.items():
                g.add_edge(u, v, weight)
        return g

    def vertices(self):
        for v in self._vertices:
            yield v

    def edges(self):
        for u, adj in self.items():
            for v, weight in adj.items():
                yield (u, v, weight)

    def add_edge(self, u: T, v: T, weight: int):
        if u not in self._g:
            self._g[u] = {}

        self._g[u][v] = weight
        self._vertices.add(u)
        self._vertices.add(v)

    def add_undirected_edge(self, u: T, v: T, weight: int):
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def wfs(
        self,
        s: T,
        bag: Bag,
        visit: Callable[[T], None] = lambda _: None,
    ) -> Dict[T, Optional[T]]:
        # whatever first search
        assert bag.is_empty()

        bag.push((None, s))
        visited = set()
        parent = {}
        while not bag.is_empty():
            prev, v = bag.pop()

            if v not in visited:
                visit(v)
                visited.add(v)
                parent[v] = prev
                for w in self[v]:
                    bag.push((v, w))

        return parent
