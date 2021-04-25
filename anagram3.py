"""
BRUTE FORCE

A brute force technique for solving a problem typically
tries to exhaust all possibilities. For the anagram
detection problem, we can simply generate a list of all
possible strings using the characters from s1 and then
see if s2 occurs.

The total number of candidate strings is
n∗(n−1)∗(n−2)∗...∗3∗2∗1, which is n!. Although some of
the strings may be duplicates, the program cannot know
this ahead of time and so it will still generate n!
different strings.

It turns out that n! grows even faster than 2^n as n
gets large.
"""
candidates = []


def permutations(remaining, candidate=""):

    if len(remaining) == 0:
        candidates.append(candidate)

    for i in range(len(remaining)):
        new_candidate = candidate + remaining[i]
        new_remaining = remaining[0:i] + remaining[i+1:]
        permutations(new_remaining, new_candidate)
    return candidates


def anagram(s1, s2):
    candidates = permutations(s1)
    print(candidates)
    if s2 not in candidates:
        return False
    else:
        return True


print(anagram('ABC', 'BCA'))
