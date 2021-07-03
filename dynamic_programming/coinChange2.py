# Dynamic Programming bottoms up manner (Tabular)
# Time Complexity: O(mn)


def coin_change(coins: list, n: int, target:int) -> int:
    # We need target + 1 rows as the table is made
    # in bottom up manner using the base case 0 value
    # case (n = 0)
    dp = [[0 for i in range(n)] for j in range(target + 1)]

    # Fill the entries for 0 value case
    for i in range(n):
        dp[0][i] = 1

    for i in range(1, target + 1):
        for j in range(n):
            x = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
            y = dp[i][j - 1] if j >= 1 else 0
            dp[i][j] = x + y
    return dp[target][n - 1]


# Driver program to test above function
arr = [1, 2, 3]
m = len(arr)
n = 4
print(coin_change(arr, m, n))
