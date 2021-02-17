from algo.applications import (
    longest_palindrome_substring,
    maximum_subarray,
    palindrome_partitioning,
    sudoku_solver,
    sum_of_subarray_minimums,
    super_egg_drop,
    word_ladder_II,
)

from .data import big_word_ladder


def test_super_egg_drop():
    assert 23 == super_egg_drop.solve_dp(4, 10000)


def test_sum_of_subarray_minimums():
    assert 17 == sum_of_subarray_minimums.solve([3, 1, 2, 4])
    assert 20 == sum_of_subarray_minimums.solve([1, 2, 3, 4])


def test_maximum_subarray():
    def check(arr, ans):
        assert ans == maximum_subarray.solve_dc(arr)
        assert ans == maximum_subarray.solve_dp(arr)

    check([3, 0, 0, 2, 2], 7)
    check([1, -1, 1], 1)
    check([8, -19, 5, -4, 20], 21)
    check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    check([2, -1, 2, 1, 3, -2, 1, 2, 1, -2], 9)


def test_palindrome_partitioning():
    def check(s, ans):
        assert set(palindrome_partitioning.solve(s)) == set(ans)

    check("aah", [("aa", "h"), ("a", "a", "h")])


def test_longest_palindrome_substring():
    assert "ABA" == longest_palindrome_substring.solve("ABABD")


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


def test_word_ladder():
    def check(start, end, words, ans):
        assert sorted(word_ladder_II.solve(start, end, words)) == sorted(ans)

    check(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"],
        [["hit", "hot", "lot", "log", "cog"], ["hit", "hot", "dot", "dog", "cog"]],
    )
    check("a", "c", ["a", "b", "c"], [["a", "c"]])
    check(
        "leet",
        "code",
        ["lest", "leet", "lose", "code", "lode", "robe", "lost"],
        [["leet", "lest", "lost", "lose", "lode", "code"]],
    )
    check(
        "game",
        "thee",
        ["frye", "heat", "tree", "thee", "game", "free", "hell", "fame", "faye"],
        [["game", "fame", "faye", "frye", "free", "tree", "thee"]],
    )
    check(
        "ta",
        "if",
        ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"],
        [
            ["ta", "ca", "cf", "if"],
            ["ta", "ha", "hf", "if"],
            ["ta", "to", "io", "if"],
            ["ta", "ts", "is", "if"],
        ],
    )
