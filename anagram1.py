"""
CHECKING OFF

First solution to the anagram problem will check the
lengths of the strings and then to see that each
character in the first string actually occurs in
the second. If it is possible to “checkoff” each
character, then the two strings must be anagrams.


The complexity of this solution is of the order O(n^2).
"""


def anagram(s1, s2):
    is_anagram = True
    if len(s1) != len(s2):
        is_anagram = False

    ls = list(s2)
    i = 0
    while i < len(s1) and is_anagram:
        j = 0
        found = False
        while j < len(ls) and not found:
            if s1[i] == ls[j]:
                found = True
            else:
                j += 1
        if found:
            ls[j] = None
        else:
            is_anagram = False

        i += 1
    return is_anagram


print(anagram('abcd', 'dcba'))
