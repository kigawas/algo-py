from algo.applications import sum_of_subarray_minimums, trapping_rain_water


def test_sum_of_subarray_minimums():
    assert 17 == sum_of_subarray_minimums.solve([3, 1, 2, 4])
    assert 20 == sum_of_subarray_minimums.solve([1, 2, 3, 4])


def test_trapping_rain_water():
    assert 6 == trapping_rain_water.solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert 9 == trapping_rain_water.solve([4, 2, 0, 3, 2, 5])
