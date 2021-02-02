from algo.data_structures.graph import Graph


def test_graph():
    g: Graph[str] = Graph()
    g.add_edge("a", "b", 1)

    assert g["a"]["b"] == 1
    assert g["a"]["b"] == 1

    for u, adj in g.items():
        for v, w in adj.items():
            assert g[u][v] == w

    d = {"a": {"b": 1}, "b": {"a": 1}}
    assert Graph.from_dict(d) == g
