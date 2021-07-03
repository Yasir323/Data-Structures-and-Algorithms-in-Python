# Write a recusrsive function to reverse a list
import time
import sys

sys.setrecursionlimit(10**6)


def reverse(ls1):
    if len(ls1) <= 1:
        return ls1
    else:
        ls1[0], ls1[-1] = ls1[-1], ls1[0]
        return [ls1[0]] + reverse(ls1[1:-1]) + [ls1[-1]]


# def reverse(ls1):
#     if len(ls1) < 1:
#         return []
#     return [ls1[-1]] + reverse(ls1[:-1])


# ls = [*range(2000)]
ls = [1, 2, 3, 4]
start_time = time.time()
print(reverse(ls))
stop_time = time.time()
print(f"Total time taken: {(stop_time - start_time) * 1000} msec.")
