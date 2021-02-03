from typing import Callable

from algo.data_structures.bag import Queue, Stack
from algo.data_structures.graph import Graph


def dfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    return graph.wfs(s, Stack(), visit)


def bfs(graph: Graph, s: int, visit: Callable = lambda n: print(n)):
    return graph.wfs(s, Queue(), visit)
