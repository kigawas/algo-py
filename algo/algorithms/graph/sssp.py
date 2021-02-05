# single source shortest paths

from typing import Callable, Dict

from algo.data_structures.bag import PriorityQueue
from algo.data_structures.graph import Graph, T


def relax(dist: Dict[T, int], u: T, v: T, weight: int):
    if v not in dist or dist[v] > dist[u] + weight:
        dist[v] = dist[u] + weight
        return True
    return False


def ford(graph: Graph, s: int):
    dist = {s: 0}
    parent = {s: None}

    V = len(list(graph.vertices()))
    for _ in range(V - 1):
        for u, v, weight in graph.edges():
            if relax(dist, u, v, weight):
                parent[v] = u

    for u, v, weight in graph.edges():
        if dist[v] > dist[u] + weight:
            # negative cycle!
            raise ValueError("negative cycle")
    return dist, parent


def dijkstra(
    graph: Graph,
    s: int,
    visit: Callable = lambda n, d: print(n, d),
):
    dist = {s: 0}

    def score(u, v, weight):
        relax(dist, u, v, weight)
        return dist[v]

    parent = graph.pqs(s, PriorityQueue(), 0, score, visit)
    return dist, parent
