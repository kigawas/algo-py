from algo.algorithms.math.prime import fermat_check
from algo.algorithms.math.prime import linear
from algo.algorithms.math.prime import miller_rabin_check
from algo.algorithms.math.prime import sqrt_check
from algo.algorithms.math.prime import trial_division


def test_prime():
    primes = linear(1000)
    for p in primes:
        assert trial_division(p)
        assert fermat_check(p)
        assert sqrt_check(p)
        assert miller_rabin_check(p)


def test_mr_check():
    n = 100000
    primes = set(linear(n))
    for i in range(n):
        if i not in primes:
            assert not miller_rabin_check(i)
        else:
            assert miller_rabin_check(i)
