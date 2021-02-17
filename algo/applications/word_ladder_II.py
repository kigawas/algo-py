def solve(start, end, word_list):
    n = len(word_list)
    l = len(end)
    res = []
    res_len = n + 2
    import string

    def diff(wa, wb):
        assert len(wa) == len(wb)
        count = 0
        for ca, cb in zip(wa, wb):
            if ca != cb:
                count += 1
        return count

    def bt(ans, remaining_words):
        # print(ans, remaining_words)
        nonlocal res_len
        if ans[-1] == end:
            res.append(ans)
            res_len = len(ans)
            return True
        elif len(remaining_words) == 0 or len(ans) >= res_len:
            return False

        expanded = set()
        for w in remaining_words:
            d = diff(w, end)
            if d <= diff(ans[-1], end) and d <= n - len(ans):
                # prune
                expanded.add(w)

        for w in expanded:
            if (
                diff(ans[-1], w) == 1
                # and diff(w, end) <= diff(ans[-1], end)
                and len(ans) <= res_len
            ):
                bt(ans + [w], expanded - {w})

        return False

    words = set(word_list)
    if end not in words:
        return []
    bt([start], words)
    return [r for r in res if len(r) <= res_len]
