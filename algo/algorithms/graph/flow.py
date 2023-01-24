# maximum flow & minimum cut
from algo.data_structures.bag import PriorityQueue, Queue
from algo.data_structures.graph import Graph, T

INT_MAX = 1 << 30


class ResidualGraph(Graph[T, int]):
    def add_edge(self, u: T, v: T, cap: int):
        super().add_edge(u, v, cap)
        super().add_edge(v, u, 0)

    def add_flow(self, u: T, v: T, delta_flow: int):
        self[u][v] -= delta_flow
        self[v][u] += delta_flow


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
        df = dfs(s, INT_MAX)
        if df > 0:
            flow += df
        else:
            break

    return flow


def edmonds_karp(graph: ResidualGraph[T], s: T, t: T) -> int:
    # just best first search with largest bottleneck value
    # ref: UIUC algorithms P340
    # N.B.: simple bfs without priority queue also works

    def bfs():
        prev = {s: None}

        pq = PriorityQueue()
        pq.push(s)

        while not pq.is_empty():
            v, _ = pq.pop()
            for w, w_cap in graph[v].items():
                if w_cap > 0 and w not in prev:
                    pq.push(w, w_cap)
                    prev[w] = v
        return prev

    flow = 0
    while True:
        prev = bfs()
        if t in prev:
            df = INT_MAX  # delta flow
            cur: T = t
            while prev[cur] is not None:
                cap = graph[prev[cur]][cur]  # type:ignore
                df = min(df, cap)
                cur = prev[cur]  # type:ignore

            cur: T = t
            while prev[cur] is not None:
                graph.add_flow(prev[cur], cur, df)  # type:ignore
                cur = prev[cur]  # type:ignore
            flow += df
        else:
            break

    return flow


def dinitz(graph: ResidualGraph[T], s: T, t: T) -> int:  # noqa
    # advanced edmonds karp
    # use bfs to label before finding augmenting paths with dfs

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
                df = dfs(w, min(flow, cap))  # min flow stating from w

                if df > 0:
                    # only return when answer is valid
                    graph.add_flow(v, w, df)
                    return df

        return 0

    flow = 0
    while True:
        levels = bfs()

        if t not in levels:
            # no path in residual graph to t
            return flow

        while True:
            df = dfs(s, INT_MAX)
            if df > 0:
                flow += df
            else:
                break
