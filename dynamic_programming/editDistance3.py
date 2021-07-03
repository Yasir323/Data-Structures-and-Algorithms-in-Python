def edit_distance(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    dp = [[0 for i in range(len1 + 1)] for j in range(2)]

    # Base condition when the second string is empty
    for i in range(len1 + 1):
        dp[0][i] = i

    # Start filling the dp
    # This loop runs for every char
    # in the 2nd string
    for i in range(1, len2 + 1):
        for j in range(len1 + 1):
            # If 1st string is empty
            # Add all characters to get 2nd
            if j == 0:
                dp[i % 2][j] = i

            # If char from both string is same
            # then we do not perform any operation
            elif str1[j - 1] == str2[i - 1]:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1]

            # If the char from btoh strings are not same
            # then we take minimum from 3 specified
            # operations
            else:
                dp[i % 2][j] = 1 + min(
                    dp[(i - 1) % 2][j],  # Remove
                    dp[i % 2][j - 1],  # Insert
                    dp[(i - 1) % 2][j - 1]  # Replace
                )
    return dp[len2 % 2][len1]


# Driver code
str1 = "sunday"
str2 = "saturday"

print(edit_distance(str1, str2))
