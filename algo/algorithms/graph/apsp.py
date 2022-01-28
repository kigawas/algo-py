# all pairs shortest paths

from algo.data_structures.graph import Graph, T


def floyd_warshall(graph: Graph[T, int]) -> dict[T, dict[T, int]]:
    # dynamic programming
    dist = {}
    for u in graph.vertices():
        for v in graph.vertices():
            if u not in dist:
                dist[u] = {}
            dist[u][v] = graph[u].get(v, -1)

    for inter in graph.vertices():
        for u in graph.vertices():
            for v in graph.vertices():
                if dist[u][inter] == -1 or dist[inter][v] == -1:
                    continue

                inter_d = dist[u][inter] + dist[inter][v]
                if dist[u][v] == -1 or dist[u][v] > inter_d:
                    dist[u][v] = inter_d

    return dist
