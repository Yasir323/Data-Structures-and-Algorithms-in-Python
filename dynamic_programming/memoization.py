"""
This is identical to the hacky default parameter method
in fibonacci.py, but in this case we ensure the cache
is retained across function calls by making it global.
"""

global_cache = {}


def fib_global_memoized(n):
    global global_cache
    if n in global_cache:
        ans = global_cache[n]
    elif n <= 2:
        ans = 1
        global_cache[n] = ans
    else:
        ans = fib_global_memoized(n - 2) + fib_global_memoized(n - 1)
        global_cache[n] = ans

    return ans


print(fib_global_memoized(50))
