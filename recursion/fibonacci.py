def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(50))  # It will be stuck here for minutes
# This is not an efficient implementation of fibonacci.
# It's time complexity is 2^n
