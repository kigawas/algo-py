from algo.applications import sum_of_subarray_minimums, super_egg_drop


def test_super_egg_drop():
    assert 23 == super_egg_drop.solve_by_dp(4, 10000)


def test_sum_of_subarray_minimums():
    assert 17 == sum_of_subarray_minimums.solve([3, 1, 2, 4])
    assert 20 == sum_of_subarray_minimums.solve([1, 2, 3, 4])
