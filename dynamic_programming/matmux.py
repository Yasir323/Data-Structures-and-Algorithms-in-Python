"""
Given a sequence of matrices, find the most efficient
way to multiply these matrices together. The problem
is not actually to perform the multiplications, but
merely to decide in which order to perform the
multiplications.
"""
# NAIVE RECUSRION APPROACH
import sys


def matmux(arr, i, j):
    if i == j:
        return 0

    min_ = sys.maxsize

    for k in range(i, j):
        count = matmux(arr, i, k) +\
            matmux(arr, k + 1, j) +\
            arr[i - 1] * arr[k] * arr[j]

        if count < min_:
            min_ = count

    return min_


# Driver code
arr = [1, 2, 3, 4, 3]
n = len(arr)

print("Minimum number of multiplications is ",
      matmux(arr, 1, n-1))
