from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Dict, Iterator, TypeVar

T = TypeVar("T", str, int)
G = Dict[Any, Dict[Any, int]]


class Graph(Mapping[T, Dict[T, int]]):
    def __init__(self) -> None:
        self._g: Dict[T, Dict[T, int]] = {}

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
    def from_dict(cls, d: G) -> Graph:
        g = cls()
        for u, adj in d.items():
            for v, weight in adj.items():
                g.add_edge(u, v, weight, undirected=False)
        return g

    def add_edge(self, u: T, v: T, weight: int, undirected: bool = True):
        if u not in self._g:
            self._g[u] = {}
        self._g[u][v] = weight

        if undirected:
            if v not in self._g:
                self._g[v] = {}
            self._g[v][u] = weight
