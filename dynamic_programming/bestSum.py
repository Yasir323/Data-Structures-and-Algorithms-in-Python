# Program to find the shortest route if any to
# a target sum given an array of numbers.
import functools


@functools.lru_cache()
def best_sum(target, numbers):
    if target == 0:
        return []
    if target < 0:
        return -1

    best_combination = -1
    for number in numbers:
        remainder = target - number
        remainder_combination = best_sum(remainder, numbers)
        if remainder_combination != -1:
            combination = remainder_combination + [number]
            if best_combination == -1 or len(combination) < len(best_combination):
                best_combination = combination
    return best_combination


print(best_sum(7, (2, 3)))
print(best_sum(7, (5, 3, 4, 7)))
print(best_sum(7, (2, 4)))
print(best_sum(8, (1, 4, 5)))
print(best_sum(100, (1, 2, 5, 25)))
