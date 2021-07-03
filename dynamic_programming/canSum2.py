# Program to find if the numbers given can add
# up to a given target or not

"""
m = target, determines the height of the tree
n = array length, determines complexity
This has a O(n^m) time complexity and O(m)
space complexity when solving without memoization.

Memoized Solution:
Time = O(m*n)
Space = O(m)
"""
cache = {}


def can_sum(target, numbers):
    global cache
    if target in cache:
        return cache[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for number in numbers:
        remainder = target - number
        if can_sum(remainder, numbers):
            cache[target] = True
            return True
    cache[target] = False
    return False


print(can_sum(7, (2, 3)))
cache.clear()
print(can_sum(7, (5, 3, 4, 7)))
cache.clear()
print(can_sum(7, (2, 4)))
cache.clear()
print(can_sum(8, (2, 3, 5)))
cache.clear()
print(can_sum(300, (7, 14)))
