from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable, Dict, Iterator, Optional, Tuple, TypeVar

from .bag import Bag, PriorityQueue

T = TypeVar("T", str, int)
ScoreT = TypeVar("ScoreT", int, float)
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

    def vertices(self):
        sources = self.keys()

        seen = set()
        for u in sources:
            yield u
            seen.add(u)

        for adj in self.values():
            for v in adj:
                if v not in seen:
                    seen.add(v)
                    yield v

    def edges(self):
        for u, adj in self.items():
            for v, weight in adj.items():
                yield (u, v, weight)

    def add_edge(self, u: T, v: T, weight: int, undirected: bool = True):
        if u not in self._g:
            self._g[u] = {}
        self._g[u][v] = weight

        if undirected:
            if v not in self._g:
                self._g[v] = {}
            self._g[v][u] = weight

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

    def pqs(
        self,
        s: T,
        pq: PriorityQueue[Tuple[ScoreT, Tuple[Optional[T], T]]],
        init_score: ScoreT,
        score: Callable[[T, T, ScoreT], ScoreT],
        visit: Callable[[T, ScoreT], None] = lambda x, y: None,
    ) -> Dict[T, Optional[T]]:
        # best first search
        assert pq.is_empty()

        pq.push((None, s), init_score)
        visited = set()
        parent = {}
        while not pq.is_empty():
            (prev, v), current_score = pq.pop()
            if v not in visited:
                visited.add(v)
                parent[v] = prev
                visit(v, current_score)
                for w, weight in self[v].items():
                    new_score = score(v, w, weight)
                    pq.push((v, w), new_score)
        return parent
