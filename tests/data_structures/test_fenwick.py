from random import shuffle

from algo.data_structures.fenwick import Fenwick


def test_fenwick():
    def check(A):
        shuffle(A)
        prefix = [0]
        s = 0
        for a in A:
            s += a
            prefix.append(s)

        f = Fenwick(A)
        assert f.ask(0) == 0
        for i in range(len(A) + 1):
            assert f.ask(i) == prefix[i]

    check([1, 2, 3, 4, 5])
    check(list(range(100)))
