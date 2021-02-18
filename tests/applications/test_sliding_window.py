from algo.applications import longest_palindrome_substring


def test_longest_palindrome_substring():
    assert "ABA" == longest_palindrome_substring.solve("ABABD")
