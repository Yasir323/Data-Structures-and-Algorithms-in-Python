# Program to calculate the factorial
# Itertive solution
def factorial_iter(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result


print(factorial_iter(5))


# Recursive solution
def factorial_recusrive(num):
    if num <= 1:
        return 1
    return num * factorial_recusrive(num - 1)


print(factorial_recusrive(5))
