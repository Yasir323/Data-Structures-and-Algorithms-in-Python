# Largest Incresing Subsequence Problem using DP\
# This solution has a O(n^2) time complexity

def lis(arr):
    n = len(arr)
    lis = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0

    for l in lis:
        maximum = max(maximum, l)

    return maximum


arr = [50, 3, 10, 7, 40, 80]
print(lis(arr))
