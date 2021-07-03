# Memoized approach
import sys

def matmux(p, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize
    for k in range(i, j):
        dp[i][j] = min(
            dp[i][j],
            matmux(p, i, k) + matmux(p, k + 1, j) +\
                p[i - 1] * p[k] * p[j]
        )
    return dp[i][j]

# Driver Code
arr = [1, 2, 3, 4]
n = len(arr)
dp = [[-1 for i in range(n)] for j in range(n)]
print("Minimum number of multiplications is", matmux(arr, 1, n - 1))
