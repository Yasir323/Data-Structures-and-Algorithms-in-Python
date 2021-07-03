# Program to return any combination that
# adds up to a number, 'targetSum'

"""
m = target, determines the height of the tree
n = array length, determines complexity
This has a O(n^m * m) time complexity and O(m)
space complexity when solving without memoization.

Memoized Solution:
Time = O(m*n*m)
Space = O(m*m)
"""
import functools


@functools.lru_cache()
def how_sum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return -1

    for number in numbers:
        remainder = target - number
        remainder_result = how_sum(remainder, numbers)
        if remainder_result != -1:
            return remainder_result + [number]
    return -1


print(how_sum(7, (2, 3)))
print(how_sum(7, (5, 3, 4, 7)))
print(how_sum(7, (2, 4)))
print(how_sum(8, (2, 3, 5)))
print(how_sum(300, (7, 14)))
