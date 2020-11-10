from collections import deque
from heapq import heappop
from heapq import heappush
from typing import Callable
from typing import Deque
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

Vertex = Tuple[Optional[int], int]


def dfs(graph: Dict[int, List[int]], s: int, visit: Callable = lambda n: print(n)):
    visited = set()
    bag: List[Vertex] = [(None, s)]
    parent = {}
    while bag:
        p, v = bag.pop()
        if v not in visited:
            visit(v)
            visited.add(v)
            parent[v] = p
            for w in graph.get(v, []):
                bag.append((v, w))

    return parent


def bfs(graph: Dict[int, List[int]], s: int, visit: Callable = lambda n: print(n)):
    visited = set()
    bag: Deque[Vertex] = deque([(None, s)])
    parent = {}
    while bag:
        p, v = bag.popleft()
        if v not in visited:
            visit(v)
            visited.add(v)
            parent[v] = p
            for w in graph.get(v, []):
                bag.append((v, w))
    return parent


def shortest_paths(
    graph: Dict[int, List[Tuple[int, int]]],
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
            for (w, weight) in graph.get(v, []):
                if w not in dist or dist[w] > dist[v] + weight:
                    dist[w] = dist[v] + weight
                heappush(bag, (dist[w], w))
