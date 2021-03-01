from algo.applications import (
    coin_change,
    coin_change_2,
    maximum_subarray,
    ones_and_zeros,
    partition_equal_subset_sum,
    super_egg_drop,
    target_sum,
    word_break,
)


def test_super_egg_drop():
    assert 23 == super_egg_drop.solve_dp(4, 10000)


def test_maximum_subarray():
    def check(arr, ans):
        assert ans == maximum_subarray.solve_dp(arr)

    check([3, 0, 0, 2, 2], 7)
    check([1, -1, 1], 1)
    check([8, -19, 5, -4, 20], 21)
    check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    check([2, -1, 2, 1, 3, -2, 1, 2, 1, -2], 9)


def test_word_break():
    assert (
        word_break.solve(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            [
                "aa",
                "aaa",
                "aaaa",
                "aaaaa",
                "aaaaaa",
                "aaaaaaa",
                "aaaaaaaa",
                "aaaaaaaaa",
                "aaaaaaaaaa",
                "ba",
            ],
        )
        is False
    )

    assert word_break.solve("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


def test_partition_equal_subset_sum():
    def check(nums, ans):
        assert partition_equal_subset_sum.solve_dp_naive(nums) is ans
        assert partition_equal_subset_sum.solve_dp(nums) is ans

    check([1, 5, 5, 11], True)
    check([2, 2, 4, 10], False)
    check([2, 13, 1], False)


def test_coin_change():
    def check(coins, amount, ans):
        assert coin_change.solve_dp_naive(coins, amount) == ans
        assert coin_change.solve_dp(coins, amount) == ans

    check([1], 1, 1)
    check([1], 2, 2)
    check([1, 2, 5], 11, 3)
    check([2], 3, -1)

    assert coin_change_2.solve([1, 2, 5], 5) == 4


def test_ones_and_zeros():
    assert ones_and_zeros.solve(["10", "0001", "111001", "1", "0"], 5, 3) == 4
    assert ones_and_zeros.solve(["10", "0001", "111001", "1", "0"], 4, 3) == 3


def test_target_sum():
    assert target_sum.solve_dp([1, 1, 1, 1, 1], 3) == 5
    assert target_sum.solve_dp([1], 2) == 0
    assert target_sum.solve_dp([1, 1], -2) == 1
    assert target_sum.solve_dp([1, 2, 7, 9, 981], 1000000000) == 0
