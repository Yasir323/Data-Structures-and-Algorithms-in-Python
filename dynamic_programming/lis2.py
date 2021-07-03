# Program to print LIS using DP
def print_lis(arr):
    print("[", end="")
    for a in arr:
        print(a, end=", ")
    print("]")


def lis(arr, n):
    l = [[] for i in range(n)]
    l[0].append(arr[0])
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and len(l[i]) < len(l[j]) + 1:
                l[i] = l[j].copy()

        l[i].append(arr[i])

    maximum = l[0]

    for x in l:
        if len(x) > len(maximum):
            maximum = x

    print_lis(maximum)


arr = [50, 3, 10, 7, 40, 80]
n = len(arr)

# construct and print LIS of arr
lis(arr, n)
