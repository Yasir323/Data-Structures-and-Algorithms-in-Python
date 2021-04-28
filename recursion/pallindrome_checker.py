def remove_punctuation(str):
    punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in str:
        if char not in punctuations:
            result += char
    return result


def is_palindrome(str):
    if len(str) <= 1:
        return True
    else:
        if str[0] == str[-1]:
            return is_palindrome(str[1:-1])
        else:
            return False


print(is_palindrome(remove_punctuation("x")))
print(is_palindrome(remove_punctuation("radar")))
print(is_palindrome(remove_punctuation("hello")))
print(is_palindrome(remove_punctuation("")))
print(is_palindrome(remove_punctuation("hannah")))
print(is_palindrome(remove_punctuation("madam i'm adam")))
