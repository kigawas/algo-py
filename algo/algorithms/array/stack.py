from typing import Callable


def monotonic(
    array_length: int,
    should_pop: Callable[[int, list[int]], bool],
):
    mono: list[int] = []
    for index in range(array_length):
        while mono and should_pop(index, mono):
            mono.pop()
        mono.append(index)
