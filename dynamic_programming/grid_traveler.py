"""
Find the number of ways in which one can travel
from top left corner of the grid (n, m) to bottom
right, given that only moves that are allowed are
'down' and 'right'.

Using recusrion the time complexity of this problem
is of the order O(2^(n+m)) and O(n + m) space
complexity, but after using Memoization it becomes
O(m * n) time and O(n + m) space complexity.
"""
import functools


@functools.lru_cache()
def grid_traveler(n, m):
    if n == 1 or m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    return grid_traveler(n - 1, m) + grid_traveler(n, m - 1)


print(grid_traveler(0, 0))
print(grid_traveler(0, 1))
print(grid_traveler(1, 0))
print(grid_traveler(1, 4))
print(grid_traveler(5, 1))
print(grid_traveler(2, 2))
print(grid_traveler(2, 3))
print(grid_traveler(5, 5))
print(grid_traveler(18, 18))
