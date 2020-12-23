from algo.data_structures.union_find import UF


def test_uf():
    N = 100000
    uf = UF(N)
    for i in range(N - 1):
        uf.union(i, i + 1)
    assert uf.same(0, N - 1)
