from typing import Any
from typing import Callable
from typing import Optional
from typing import Tuple

from algo.data_structures.bag import PriorityQueue
from algo.data_structures.bag import Queue
from algo.data_structures.bag import Stack
from algo.data_structures.graph import Graph

Vertex = Tuple[Optional[Any], Any]


def dfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    return graph.wfs(s, Stack(), visit)


def bfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    return graph.wfs(s, Queue(), visit)


def shortest_paths(
    graph: Graph,
    s: int,
    visit: Callable = lambda n, d: print(n, d),
):
    dist = {s: 0}

    def score(v, w, weight):
        if w not in dist or dist[w] > dist[v] + weight:
            dist[w] = dist[v] + weight
        return dist[w]

    return graph.pqs(s, PriorityQueue(), 0, score, visit)
