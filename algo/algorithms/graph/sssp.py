# single source shortest paths
from typing import Callable, Optional

from algo.data_structures.bag import PriorityQueue
from algo.data_structures.graph import Graph, T


def relax(dist: dict[T, int], u: T, v: T, weight: int):
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
    # best first search
    # this is almost SPFA with priority queue
    pq = PriorityQueue[int]()
    pq.push(s, 0)

    dist = {s: 0}
    parent: dict[int, Optional[int]] = {s: None}

    while not pq.is_empty():
        v, current_score = pq.pop()
        visit(v, current_score)
        for w, weight in graph[v].items():
            if relax(dist, v, w, weight):
                parent[w] = v
                pq.push(w, dist[w])

    return dist, parent
