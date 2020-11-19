from random import randint
from typing import List


def linear(N: int) -> List[int]:
    sieve = [False] * N
    primes = []

    for i in range(2, N):
        if not sieve[i]:
            primes.append(i)

        for p in primes:
            if i * p >= N:
                break
            sieve[i * p] = True
            if i % p == 0:
                break

    return primes


def trial_division(n: int) -> bool:
    for d in range(2, n // 2):
        if d * d > n:
            # only run d <= sqrt(n)
            break

        if n % d == 0:
            return False

    return True


def sqrt_check(n: int) -> bool:
    # may fail
    if n < 2:
        return False
    for i in range(2, n - 1):
        if i * i % n == 1:
            return False
    return True


def fermat_check(n: int) -> bool:
    # may fail
    if n < 2:
        return False
    elif n == 2:
        return True

    a = randint(2, n - 1)
    return pow(a, n - 1, n) == 1


def miller_rabin_check(n: int) -> bool:
    # may fail
    if n < 2:
        return False
    elif n == 2:
        return True

    u, t = n - 1, 0
    while u % 2 == 0:
        u >>= 1
        t += 1

    def witness(a: int) -> bool:
        if a in (0, 1, n - 1):
            return True

        x = pow(a, u, n)  # x = a^u mod n
        if x == 1 or x == n - 1:
            # fermat
            return True

        for _ in range(0, t):
            x = x * x % n
            if x == n - 1:
                return True
        return False

    possible_a = [2, 7, 61]  # sprp, correctly check prime under n < 4,759,123,141
    return all([witness(a % n) for a in possible_a])
