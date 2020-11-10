from algo.algorithms.graph.search import bfs
from algo.algorithms.graph.search import dfs
from algo.algorithms.graph.search import shortest_paths

graph = {
    1: [2, 3],
    2: [3, 4],
}


def test_dfs():
    res = []
    dfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 3, 2, 4]


def test_bfs():
    res = []
    bfs(graph, 1, lambda n: res.append(n))
    assert res == [1, 2, 3, 4]


def test_best_search():
    graph = {
        1: [(2, 3), (3, 5)],
        2: [(3, 1), (4, 3)],
        3: [(4, 1)],
    }
    dist = {}
    shortest_paths(
        graph,
        1,
        lambda n, d: dist.update({n: d}),
    )
    assert dist[4] == 5
