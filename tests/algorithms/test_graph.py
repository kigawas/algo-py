from algo.algorithms.graph.search import bfs, dfs, shortest_paths
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


def test_best_search():
    graph = Graph.from_dict(
        {
            1: {2: 5, 3: 3},
            2: {3: 1, 4: 3},
            3: {4: 1},
        }
    )
    dist = {}
    res = []

    def visit(n, d):
        res.append(n)
        dist[n] = d

    par = shortest_paths(graph, 1, visit)
    assert dist[4] == 4
    assert res == [1, 3, 4, 2]

    path = []

    v = 4
    while v is not None:
        path.append(v)
        v = par[v]

    assert path[::-1] == [1, 3, 4]
