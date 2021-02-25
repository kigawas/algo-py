"""
https://leetcode.com/problems/word-ladder-ii/
"""


def solve(start, end, word_list):
    n = len(word_list)
    res = []
    words = set(word_list)

    if end not in words:
        return []

    import string
    from collections import deque

    def bfs():
        dist = {}
        for w in words:
            dist[w] = n + 2  # max length
        dist[start] = 0

        q = deque([(start, [start])])
        while q:
            cur, path = q.popleft()
            if cur == end:
                res.append(path)
                continue

            for i in range(len(end)):
                for c in string.ascii_lowercase:
                    candidate = cur[:i] + c + cur[i + 1 :]
                    is_valid = candidate != cur and candidate in words
                    if is_valid and dist[candidate] >= len(path):  # prune
                        dist[candidate] = len(path)
                        q.append((candidate, path + [candidate]))

    bfs()

    return res
