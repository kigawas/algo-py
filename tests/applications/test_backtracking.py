from algo.applications import (
    coin_change,
    palindrome_partitioning,
    partition_equal_subset_sum,
    partition_to_k_equal_sum_subsets,
    permutations,
    restore_ip_address,
    sudoku_solver,
    word_break_II,
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


def test_restore_ip_address():
    assert restore_ip_address.solve("25525511135") == [
        "255.255.11.135",
        "255.255.111.35",
    ]
    assert restore_ip_address.solve("1111") == ["1.1.1.1"]
    assert restore_ip_address.solve("111111111111") == ["111.111.111.111"]
    assert restore_ip_address.solve("1111111111111") == []


def test_word_break():
    def check(s, words, ans):
        assert sorted(word_break_II.solve(s, words)) == sorted(ans)

    check(
        "catsanddog",
        ["cat", "cats", "and", "sand", "dog"],
        ["cats and dog", "cat sand dog"],
    )
    check(
        "pineapplepenapple",
        ["apple", "pen", "applepen", "pine", "pineapple"],
        ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
    )
    check("catsandog", ["cats", "dog", "sand", "and", "cat"], [])
    check(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        [
            "a",
            "aa",
            "aaa",
            "aaaa",
            "aaaaa",
            "aaaaaa",
            "aaaaaaa",
            "aaaaaaaa",
            "aaaaaaaaa",
            "aaaaaaaaaa",
        ],
        [],
    )


def test_permutations():
    assert permutations.solve([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_partition_equal_subset_sum():
    assert partition_equal_subset_sum.solve_bt([1, 5, 5, 11])
    assert not partition_equal_subset_sum.solve_bt([2, 2, 4, 10])


def test_coin_change():
    assert coin_change.solve_bt([1, 2, 5], 11) == 3
    assert coin_change.solve_bt([1], 2) == 2
    assert coin_change.solve_bt([333, 243, 214, 132, 281], 9334)
    assert coin_change.solve_bt([2], 3) == -1
