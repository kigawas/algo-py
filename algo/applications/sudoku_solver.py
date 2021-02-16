"""
https://leetcode.com/problems/sudoku-solver/
"""


def solve(board):  # noqa
    N = 9

    def check_row(i):
        seen = set()
        for j in range(N):
            if board[i][j] == ".":
                continue
            if board[i][j] not in seen:
                seen.add(board[i][j])
            else:
                return False
        return True

    def check_col(j):
        seen = set()
        for i in range(N):
            if board[i][j] == ".":
                continue
            if board[i][j] not in seen:
                seen.add(board[i][j])
            else:
                return False
        return True

    def check_box(i, j):
        assert i % 3 == 0 and j % 3 == 0
        seen = set()
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if board[x][y] == ".":
                    continue
                if board[x][y] not in seen:
                    seen.add(board[x][y])
                else:
                    return False
        return True

    def dfs(i, j):
        if i == j == N:
            return True
        for k in range(1, N + 1):
            board[i][j] = str(k)
            if check_row(i) and check_col(j) and check_box(i - i % 3, j - j % 3):
                if dfs(*expand()):
                    return True
            board[i][j] = "."
        return False

    def expand():
        for i in range(N):
            for j in range(N):
                if board[i][j] == ".":
                    return i, j
        return N, N

    i, j = expand()
    dfs(i, j)
    return board
