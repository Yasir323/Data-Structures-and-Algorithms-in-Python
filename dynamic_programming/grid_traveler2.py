def grid_traveler(n, m, cache={}):
    key = (n, m)
    if key in cache:
        return cache[key]
    if n == 1 or m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    cache[key] = grid_traveler(n - 1, m, cache) + grid_traveler(n, m - 1, cache)
    return cache[key]


print(grid_traveler(0, 0))
print(grid_traveler(0, 1))
print(grid_traveler(1, 0))
print(grid_traveler(1, 4))
print(grid_traveler(5, 1))
print(grid_traveler(2, 2))
print(grid_traveler(2, 3))
print(grid_traveler(5, 5))
print(grid_traveler(50, 50))
