from typing import Callable
from typing import List


def monotonic(
    array_length: int,
    should_pop: Callable[[int, List[int]], bool],
):
    mono: List[int] = []
    for index in range(array_length):
        while mono and should_pop(index, mono):
            mono.pop()
        mono.append(index)
