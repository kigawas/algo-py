from collections import deque
from heapq import heappop, heappush
from typing import Any, Callable, Deque, List, Optional, Tuple

from algo.data_structures.graph import Graph

Vertex = Tuple[Optional[Any], Any]


def dfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    visited = set()
    bag: List[Vertex] = [(None, s)]
    parent = {}
    while bag:
        p, v = bag.pop()
        if v not in visited:
            visit(v)
            visited.add(v)
            parent[v] = p
            for w in graph[v]:
                bag.append((v, w))

    return parent


def bfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    visited = set()
    bag: Deque[Vertex] = deque([(None, s)])
    parent = {}
    while bag:
        p, v = bag.popleft()
        if v not in visited:
            visit(v)
            visited.add(v)
            parent[v] = p
            for w in graph[v]:
                bag.append((v, w))
    return parent


def shortest_paths(
    graph: Graph,
    s: int,
    visit: Callable = lambda n, d: print(n, d),
):
    visited = set()
    dist = {s: 0}
    bag = [(0, s)]
    while bag:
        v_dist, v = heappop(bag)
        if v not in visited:
            visit(v, v_dist)
            visited.add(v)
            for (w, weight) in graph[v].items():
                if w not in dist or dist[w] > dist[v] + weight:
                    dist[w] = dist[v] + weight
                heappush(bag, (dist[w], w))
