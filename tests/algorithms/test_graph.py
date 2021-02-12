from algo.algorithms.graph.apsp import floyd_warshall
from algo.algorithms.graph.flow import (
    ResidualGraph,
    dinitz,
    edmonds_karp,
    fold_fulkerson,
)
from algo.algorithms.graph.search import bfs, dfs
from algo.algorithms.graph.sssp import dijkstra, ford
from algo.data_structures.graph import Graph


def test_dfs_bfs():
    g = {
        1: {2: 1, 3: 1},
        2: {3: 1, 4: 1},
    }
    graph = Graph.from_dict(g)
    res = []
    dfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 3, 2, 4]

    graph = Graph.from_dict(g)
    res = []
    bfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 2, 3, 4]


def test_sssp_apsp():
    # UIUC algorithms: P289
    g = {
        1: {2: 0, 3: -8},
        2: {3: -16, 4: 0},
        3: {4: 0, 5: -4},
        4: {5: -8},
    }
    graph = Graph.from_dict(g)

    order = []

    def visit(n, d):
        order.append((n, d))

    dist, prev = dijkstra(graph, 1, visit)
    assert dist[5] == -24
    assert order == [
        (1, 0),
        (3, -8),
        (5, -12),
        (4, -8),
        (5, -16),
        (2, 0),
        (3, -16),
        (5, -20),
        (4, -16),
        (5, -24),
    ]

    assert (dist, prev) == ford(graph, 1)

    path = []

    v = 5
    while v is not None:
        path.append(v)
        v = prev[v]

    assert path[::-1] == [1, 2, 3, 4, 5]

    graph = Graph.from_dict(g)
    dist = floyd_warshall(graph)
    assert dist[1][5] == -24


def test_flow():
    def assert_eq(g, s, t, max_flow):
        graph = ResidualGraph.from_dict(g)
        assert fold_fulkerson(graph, s, t) == max_flow

        graph = ResidualGraph.from_dict(g)
        assert edmonds_karp(graph, s, t) == max_flow

        graph = ResidualGraph.from_dict(g)
        assert dinitz(graph, s, t) == max_flow

    # UIUC algorithms: P330
    g = {
        1: {2: 20, 3: 10},
        2: {3: 10, 4: 5},
        3: {5: 10},
        4: {3: 15, 6: 15},
        5: {4: 10, 6: 20},
    }
    assert_eq(g, 1, 6, 15)

    # UIUC algorithms: P338
    g = {
        1: {2: 9, 3: 6},
        2: {3: 5, 4: 4},
        3: {4: 14},
        4: {3: 3, 6: 4},
        5: {4: 3, 6: 11},
        6: {1: 15},
    }
    assert_eq(g, 1, 6, 4)
