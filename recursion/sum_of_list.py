# Sum of list
# Iterative solution
def sum_iter(elements):
    result = 0
    for i in elements:
        result += i
    return result


print(sum_iter([*range(1, 10, 2)]))


# Recursive solution
def sum_recursive(elements):
    if len(elements) == 1:
        return elements[0]
    else:
        return elements[0] + sum_recursive(elements[1:])


print(sum_iter([*range(1, 10, 2)]))
