from algo.applications import skyline_problem


def test_skyline_problem():
    def check(buildings, ans):
        assert skyline_problem.solve(buildings) == ans

    check(
        [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
        [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]],
    )
    check([], [])
