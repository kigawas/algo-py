def string_hash(s: str) -> int:
    p = 131
    m = 1 << 31
    h = 0
    for c in s:
        h = (h * p + (ord(c) - ord("a"))) % m
    return h
