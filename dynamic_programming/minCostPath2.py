# Dynamic Programming Python implementation of Min Cost Path
# problem
ROW = 3
COLUMN = 3

def min_cost(cost, m, n):
    dp = [[0 for x in range(COLUMN)] for y in range(ROW)]
    dp[0][0] = cost[0][0]
    # Initialize first column of total cost array
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Initialize first row of total cost array
    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1] + cost[0][i]

    # Construct rest of the array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = cost[i][j] + min(
                dp[i - 1][j - 1],
                dp[i - 1][j],
                dp[i][j - 1]
            )

    return dp[m][n]


# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(min_cost(cost, 2, 2))

# Time Complexity of the DP implementation is O(mn)
# which is much better than Naive Recursive
# implementation.
