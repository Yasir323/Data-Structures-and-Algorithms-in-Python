def reverse_string(str):
    if len(str) <= 1:
        return str
    return reverse_string(str[1:]) + str[0]


print(reverse_string('radar'))
