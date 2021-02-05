# maximum flow & minimum cut
from algo.data_structures.bag import Queue
from algo.data_structures.graph import Graph, T

INT_MAX = 1 << 30


class ResidualGraph(Graph[T]):
    def add_edge(self, u: T, v: T, cap: int):
        super().add_edge(u, v, cap)
        super().add_edge(v, u, 0)

    def add_flow(self, u: T, v: T, flow: int):
        self[u][v] -= flow
        self[v][u] += flow


def dinitz(graph: ResidualGraph[T], s: T, t: T) -> int:  # noqa
    # use bfs to label before finding augmenting paths

    def bfs():
        levels = {s: 0}

        q = Queue()
        q.push(s)

        while not q.is_empty():
            v = q.pop()
            for w, cap in graph[v].items():
                if cap > 0 and w not in levels:
                    levels[w] = levels[v] + 1
                    q.push(w)
        return levels

    def dfs(v: T, flow: int) -> int:
        if v == t:
            return flow

        for w, cap in graph[v].items():
            # only expand to next level
            if cap > 0 and levels[v] < levels[w]:
                new_flow = dfs(w, min(flow, cap))  # min flow stating from w

                if new_flow > 0:
                    # only return when answer is valid
                    graph.add_flow(v, w, new_flow)
                    return new_flow

        return 0

    flow = 0
    while True:
        levels = bfs()

        if t not in levels:
            # no path in residual graph to t
            return flow

        while True:
            f = dfs(s, INT_MAX)
            if f > 0:
                flow += f
            else:
                break


def fold_fulkerson(graph: ResidualGraph[T], s: T, t: T) -> int:
    # just dfs
    seen = set()

    def dfs(v: T, flow: int):
        if v == t:
            return flow

        seen.add(v)

        for w, cap in graph[v].items():
            if cap > 0 and w not in seen:
                new_flow = dfs(w, min(flow, cap))
                if new_flow > 0:
                    graph.add_flow(v, w, new_flow)
                    return new_flow

        return 0

    flow = 0
    while True:
        seen.clear()
        f = dfs(s, INT_MAX)
        if f > 0:
            flow += f
        else:
            break

    return flow
