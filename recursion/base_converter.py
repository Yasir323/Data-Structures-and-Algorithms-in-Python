def decimal2base(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    remainder = num % base
    num = num // base
    return decimal2base(num, base) + convert_string[remainder]


print(decimal2base(1453, 16))
