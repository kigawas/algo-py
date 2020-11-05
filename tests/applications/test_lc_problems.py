from algo.applications import super_egg_drop


def test_super_egg_drop():
    assert 16 == super_egg_drop.solve_by_dp(4, 2000)
