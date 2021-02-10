from algo.applications import maximum_subarray, sum_of_subarray_minimums, super_egg_drop


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
