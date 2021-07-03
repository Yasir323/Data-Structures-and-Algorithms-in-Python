def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    result = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                result[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                result[i][j] = 1 + result[i - 1][j - 1]
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])

    return result[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))
