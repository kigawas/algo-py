from algo.applications import word_ladder_II

from .data import big_word_ladder


def test_word_ladder():
    def check(start, end, words, ans):
        assert sorted(word_ladder_II.solve(start, end, words)) == sorted(ans)

    check(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"],
        [["hit", "hot", "lot", "log", "cog"], ["hit", "hot", "dot", "dog", "cog"]],
    )
    check("a", "c", ["a", "b", "c"], [["a", "c"]])
    check(
        "leet",
        "code",
        ["lest", "leet", "lose", "code", "lode", "robe", "lost"],
        [["leet", "lest", "lost", "lose", "lode", "code"]],
    )
    check(
        "game",
        "thee",
        ["frye", "heat", "tree", "thee", "game", "free", "hell", "fame", "faye"],
        [["game", "fame", "faye", "frye", "free", "tree", "thee"]],
    )
    check(
        "ta",
        "if",
        ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"],
        [
            ["ta", "ca", "cf", "if"],
            ["ta", "ha", "hf", "if"],
            ["ta", "to", "io", "if"],
            ["ta", "ts", "is", "if"],
        ],
    )
    check("hot", "dog", ["hot", "dog"], [])
    for args in big_word_ladder():
        check(*args)
