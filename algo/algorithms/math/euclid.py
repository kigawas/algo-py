def ext_gcd(a: int, b: int) -> tuple[int, int, int]:
    # a*x + b*y = gcd(a, b)
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = ext_gcd(b, a % b)
        x = y1
        y = x1 - (y1 * (a // b))
        return g, x, y


def gcd(a: int, b: int) -> int:
    g, _, _ = ext_gcd(a, b)
    return g
