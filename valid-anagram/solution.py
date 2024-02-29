def counter(s):
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    return counter


def solution(s: str, t: str):
    """
    Is `t` an anagram of `s` ?

    An Anagram is a word or phrase formed by
    rearranging the letters of a different word
    or phrase, typically using all the original
    letters exactly once.
    """
    # Check if length is same
    if len(s) != len(t):
        return False

    # Check if each character is occured
    # exactly the sam enumber of times
    if counter(s) != counter(t):
        return False

    return True


def solution1(s: str, t: str):
    """
    Is `t` an anagram of `s` ?

    An Anagram is a word or phrase formed by
    rearranging the letters of a different word
    or phrase, typically using all the original
    letters exactly once.
    """
    return sorted(s) == sorted(t)
