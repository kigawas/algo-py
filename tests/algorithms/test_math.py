from algo.algorithms.math.euclid import ext_gcd, gcd
from algo.algorithms.math.hash import string_hash
from algo.algorithms.math.prime import (
    fermat_check,
    linear,
    miller_rabin_check,
    sqrt_check,
    trial_division,
)


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


def test_string_hash():
    assert string_hash("abc") == 133


def test_gcd():
    assert gcd(10, 24) == 2
    assert gcd(11, 0) == gcd(0, 11) == 11
    assert ext_gcd(3, 11) == (1, 4, -1)
