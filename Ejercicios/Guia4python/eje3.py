import pytest

def is_anagram(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    if len(word1) != len(word2):
        return False

    char_count = {}
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in word2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count) == 0

@pytest.mark.parametrize("word1, word2, expected_result", [
    ("listen", "silent", True),
    ("rail safety", "fairy tales", True),
    ("debit card", "bad credit", True),
    ("python", "java", False),
    ("hello", "world", False),
])

def test_is_anagram(word1, word2, expected_result):
    assert is_anagram(word1, word2) == expected_result