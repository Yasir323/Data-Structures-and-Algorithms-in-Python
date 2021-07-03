# A Naive recursive Python program to fin minimum number
# operations to convert str1 to str2


def edit_distance(str1,str2, m, n):
    # If the first string is empty. the only option
    # is to insert all characters of second string
    # into the first
    if m == 0:
        return n

    # Similarly, it goes the opposite way also
    if n == 0:
        return m

    # if last characters of the strings are the same,
    # nothing much to do. Ignore the last characters
    # and get the count for reianing strings.
    if str1[m - 1] == str2[n - 1]:
        return edit_distance(str1, str2, m - 1, n - 1)

    # If the last characters are not same, consider all
    # 3 operations (replace, remove, add) on last char
    # of 1st string, recursively and compute minimum cost
    # for all 3 operations and take minimum of 3 values.
    return 1 + min(
        edit_distance(str1, str2, m, n - 1),  # Insert
        edit_distance(str1, str2, m - 1, n),  # Remove
        edit_distance(str1, str2, m - 1, n - 1)  # Replace
    )


# Driver code
str1 = "sunday"
str2 = "saturday"
print (edit_distance(str1, str2, len(str1), len(str2)))


"""
The time complexity of above solution is exponential.
In worst case, we may end up doing O(3^m) operations.
The worst case happens when none of characters of
two strings match. Below is a recursive call diagram
for worst case.
"""
