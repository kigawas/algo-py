def gcd(a: int, b: int) -> int:
    # supposed a >= b
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    return gcd(b, a % b)
