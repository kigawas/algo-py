from algo.applications import (
    palindrome_partitioning,
    sudoku_solver,
    partition_to_k_equal_sum_subsets,
)


def test_soduku_solver():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solution = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ]
    assert sudoku_solver.solve(board) == solution


def test_palindrome_partitioning():
    def check(s, ans):
        assert set(palindrome_partitioning.solve(s)) == set(ans)

    check("aah", [("aa", "h"), ("a", "a", "h")])


def test_partition_to_k_subsets():
    assert partition_to_k_equal_sum_subsets.solve([2, 2, 2, 2, 3, 4, 5], 4) is False
    assert partition_to_k_equal_sum_subsets.solve(
        [10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3
    )
    assert partition_to_k_equal_sum_subsets.solve([4, 3, 2, 3, 5, 2, 1], 4)
    assert partition_to_k_equal_sum_subsets.solve(
        [114, 96, 18, 190, 207, 111, 73, 471, 99, 20, 1037, 700, 295, 101, 39, 649], 4
    )
