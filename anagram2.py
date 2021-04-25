"""
SORT AND COMPARE

Another solution to the anagram problem will make
use of the fact that even though s1 and s2 are different,
they are anagrams only if they consist of exactly the same
characters. So, if we begin by sorting each string
alphabetically, from a to z, we will end up with the same
string if the original two strings are anagrams.

At first glance you may be tempted to think that this
algorithm is O(n), since there is one simple iteration
to compare the n characters after the sorting process.
However, the two calls to the Python sort method are
not without their own cost. As we will see in a later
chapter, sorting is typically either O(n2) or O(nlogn),
so the sorting operations dominate the iteration. In
the end, this algorithm will have the same order of
magnitude as that of the sorting process.
"""


def anagram(s1, s2):
    ls1 = list(s1)
    ls2 = list(s2)

    ls1.sort()
    ls2.sort()

    pos = 0
    is_anagram = True

    while pos < len(s1) and is_anagram:
        if ls1[pos] == ls2[pos]:
            pos += 1
        else:
            is_anagram = False

    return is_anagram


print(anagram('abcde', 'edcba'))
