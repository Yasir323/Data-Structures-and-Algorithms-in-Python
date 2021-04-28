import functools


@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(50))

"""
Note this is simply the original function with an
extra import and a decorator. What could be simpler?
And applying this decorator gives the six orders
of magnitude speedup we expect.

The LRU in lru_cache stands for least-recently used.
It’s a FIFO approach to managing the size of the cache,
which could grow very large for functions more
complicated than fib(). But fundamentally, the approach
to memoization taken by this standard library decorator
is the same as is discussed above.

Note that fib_lru_cache is half the speed of our first
attempt at memoization.
"""
