from algo.algorithms.graph.flow import ResidualGraph, dinitz, fold_fulkerson
from algo.algorithms.graph.search import bfs, dfs
from algo.algorithms.graph.sssp import dijkstra, ford
from algo.data_structures.graph import Graph

graph = Graph.from_dict(
    {
        1: {2: 1, 3: 1},
        2: {3: 1, 4: 1},
    }
)


def test_dfs():
    res = []
    dfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 3, 2, 4]


def test_bfs():
    res = []
    bfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 2, 3, 4]


def test_sssp():
    # UIUC algorithms: P289
    graph = Graph.from_dict(
        {
            1: {2: 0, 3: -8},
            2: {3: -16, 4: 0},
            3: {4: 0, 5: -4},
            4: {5: -8},
        }
    )

    order = []

    def visit(n, d):
        order.append((n, d))

    dist, par = dijkstra(graph, 1, visit)
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

    assert (dist, par) == ford(graph, 1)

    path = []

    v = 5
    while v is not None:
        path.append(v)
        v = par[v]

    assert path[::-1] == [1, 2, 3, 4, 5]


def test_flow():
    # UIUC algorithms: P330
    g = {
        1: {2: 20, 3: 10},
        2: {3: 10, 4: 5},
        3: {5: 10},
        4: {3: 15, 6: 15},
        5: {4: 10, 6: 20},
    }
    graph = ResidualGraph.from_dict(g)
    assert fold_fulkerson(graph, 1, 6) == 15

    graph = ResidualGraph.from_dict(g)
    assert dinitz(graph, 1, 6) == 15
