def lowbit(x: int):
    # used to calculate the length of a range
    return x & -x


class Fenwick:
    # or binary indexed trees
    def __init__(self, A: list[int]) -> None:
        n = len(A)
        self._c = [0] * n

        for i, a in enumerate(A):
            self.add(i, a)

    def add(self, i: int, value: int):
        while i < len(self._c):
            self._c[i] += value
            i += lowbit(i + 1)

    def ask(self, i: int) -> int:
        res = 0
        while i >= 0:
            res += self._c[i]
            i -= lowbit(i + 1)
        return res
