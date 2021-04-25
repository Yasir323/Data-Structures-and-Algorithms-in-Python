"""
COUNT AND COMAPARE

Our final solution to the anagram problem takes
advantage of the fact that any two anagrams will
have the same number of a’s, the same number of
b’s, the same number of c’s, and so on. In order to
decide whether two strings are anagrams, we will
first count the number of times each character occurs.
Since there are 26 possible characters, we can use
a list of 26 counters, one for each possible character.
Each time we see a particular character, we will
increment the counter at that position. In the end,
if the two lists of counters are identical, the
strings must be anagrams.

Again, the solution has a number of iterations.
However, unlike the first solution, none of them
are nested. The first two iterations used to count
the characters are both based on n. The third
iteration, comparing the two lists of counts,
always takes 26 steps since there are 26 possible
characters in the strings. Adding it all up gives
us T(n)=2n+26 steps. That is O(n). We have found a
linear order of magnitude algorithm for solving
this problem.
"""


def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        # Find the value of the alphabet (0 - 25)
        pos = ord(s1[i]) - ord('a')
        # Increment the counter
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        # Find the value of the alphabet (0 - 25)
        pos = ord(s2[i]) - ord('a')
        # Increment the counter
        c2[pos] = c2[pos] + 1

    j = 0
    is_anagram = True
    while j < 26 and is_anagram:
        if c1[j] == c2[j]:
            j += 1
        else:
            is_anagram = False
    return is_anagram


print(anagram('apple', 'pleap'))
