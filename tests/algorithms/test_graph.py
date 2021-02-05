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
    graph = Graph.from_dict(
        {
            1: {2: 5, 3: 3},
            2: {3: 1, 4: 3},
            3: {4: 1},
        }
    )

    order = []

    def visit(n, d):
        order.append(n)

    dist, par = dijkstra(graph, 1, visit)
    assert dist[4] == 4
    assert order == [1, 3, 4, 2]

    assert (dist, par) == ford(graph, 1)

    path = []

    v = 4
    while v is not None:
        path.append(v)
        v = par[v]

    assert path[::-1] == [1, 3, 4]
