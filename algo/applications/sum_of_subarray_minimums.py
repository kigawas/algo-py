from typing import List

from algo.algorithms.array.stack import monotonic


def solve(A: List[int]) -> int:
    arr = [0] + A + [0]
    area = 0

    def should_pop(index: int, mono: List[int]) -> bool:
        nonlocal area

        cond = arr[mono[-1]] > arr[index]
        if cond:
            mono_right = mono[-1]
            mono_left = mono[-2]
            area += arr[mono_right] * (index - mono_right) * (mono_right - mono_left)
        return cond

    monotonic(len(arr), should_pop)
    return area % (10 ** 9 + 7)
