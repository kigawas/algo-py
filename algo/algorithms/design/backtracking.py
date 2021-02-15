def solve():
    res = []
    end_state = None

    def is_valid(state):
        pass

    def build_answer(state):
        pass

    def extend(cur_state):
        while cur_state:
            yield cur_state
            cur_state -= 1

    def f(ans, cur_state):
        if cur_state == end_state:
            res.append(ans)

        for next_state in extend(cur_state):
            if is_valid(next_state):
                new_ans = build_answer(next_state)
                f(ans + [new_ans], next_state)

    f([], 0)
    return res
