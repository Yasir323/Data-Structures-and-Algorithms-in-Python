# A Dynamic Programming based Python program for edit
# distance problem


def edit_distance(str1, str2, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # If the first string is empty, only option is
            # to insert all characters of 2nd string
            if i == 0:
                dp[i][j] = j  # Minimum operations = j

            # If the 2nd string is empty, then only option
            # is to remove all characters from the 1st string
            elif j == 0:
                dp[i][j] = i  # Minimum operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Insert
                    dp[i - 1][j],  # Remove
                    dp[i - 1][j - 1]  # Replace
                )
    return dp[m][n]


# Driver code
str1 = "sunday"
str2 = "saturday"

print(edit_distance(str1, str2, len(str1), len(str2)))

"""
Time Complexity: O(m x n)
Auxiliary Space: O(m x n)

Space Complex Solution: In the above-given method
we require O(m x n) space. This will not be suitable
if the length of strings is greater than 2000 as it
can only create 2D array of 2000 x 2000. To fill a
row in DP array we require only one row the upper
row. For example, if we are filling the i = 10 rows
in DP array we require only values of 9th row. So
we simply create a DP array of 2 x str1 length.
This approach reduces the space complexity.
"""
