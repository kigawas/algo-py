from algo.applications import maximum_subarray


def test_maximum_subarray():
    def check(arr, ans):
        assert ans == maximum_subarray.solve_dc(arr)

    check([3, 0, 0, 2, 2], 7)
    check([1, -1, 1], 1)
    check([8, -19, 5, -4, 20], 21)
    check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
    check([2, -1, 2, 1, 3, -2, 1, 2, 1, -2], 9)
