# single source shortest paths

from typing import Callable

from algo.data_structures.bag import PriorityQueue
from algo.data_structures.graph import Graph


def dijkstra(
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
