# all pairs shortest paths
from typing import Dict, Optional

from algo.data_structures.graph import Graph, T


def floyd_warshall(graph: Graph[T, int]):
    # dynamic programming
    dist: Dict[T, Dict[T, Optional[int]]] = {}
    for u in graph.vertices():
        for v in graph.vertices():
            if u not in dist:
                dist[u] = {}
            dist[u][v] = graph[u].get(v, None)

    for inter in graph.vertices():
        for u in graph.vertices():
            for v in graph.vertices():
                if dist[u][inter] is None or dist[inter][v] is None:
                    continue

                inter_d = dist[u][inter] + dist[inter][v]  # type: ignore
                if dist[u][v] is None or dist[u][v] > inter_d:  # type: ignore
                    dist[u][v] = inter_d

    return dist
