from random import shuffle

from algo.data_structures.fenwick import Fenwick


def test_fenwick():
    def check(A):
        shuffle(A)
        prefix = []
        s = 0
        for a in A:
            s += a
            prefix.append(s)

        f = Fenwick(A)
        for i, p in enumerate(prefix):
            assert f.ask(i) == p

    check([1, 2, 3, 4, 5])
    check(list(range(500)))
