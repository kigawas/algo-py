from algo.data_structures.graph import Graph


def test_graph():
    g: Graph[str] = Graph()
    g.add_undirected_edge("a", "b", 1)

    assert g["a"]["b"] == 1
    assert g["b"]["a"] == 1

    for u, adj in g.items():
        for v, w in adj.items():
            assert g[u][v] == w

    d = {"a": {"b": 1}, "b": {"a": 1}}
    assert Graph.from_dict(d) == g


def test_v_and_e():
    g: Graph[str] = Graph()
    g.add_edge("a", "b", 1)
    g.add_edge("b", "c", 2)
    g.add_edge("a", "d", 3)
    g.add_edge("d", "c", 4)
    g.add_edge("c", "a", 5)

    assert len(list(g.vertices())) == 4
    assert len(list(g.edges())) == 5
