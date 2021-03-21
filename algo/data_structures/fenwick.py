def lowbit(x: int):
    # used to calculate the length of a range
    return x & -x


class Fenwick:
    # or binary indexed trees
    def __init__(self, A: list[int]) -> None:
        # add 1 to make it left closed right open
        # i.e.
        # S[i] = ΣA[k] for k ∈ [0, i)
        #   A[0] + A[1] + ... + A[i-1]
        #   e.g. S[0] = 0, S[1] = A[0], S[2] = A[0] + A[1], ...
        # S[j] - S[i] = ΣA[k] for k ∈ [i, j)
        #   A[i] + A[i+1] + ... + A[j-1]
        #   e.g S[3] - S[1] = A[1] + A[2]
        # Ref: https://www.cs.utexas.edu/~EWD/transcriptions/EWD08xx/EWD831.html
        self._s = [0] * (1 + len(A))

        for i, a in enumerate(A):
            self.add(i + 1, a)

    def add(self, i: int, value: int):
        """
        A[i] += value
        """
        while i < len(self._s):
            self._s[i] += value
            i += lowbit(i)

    def ask(self, i: int) -> int:
        """
        ΣA[k] for k ∈ [0, i)
        """
        res = 0
        while i > 0:
            res += self._s[i]
            i -= lowbit(i)
        return res
