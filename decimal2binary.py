class Stack:

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def __len__(self):
        return len(self.items)


def base_converter(decimal, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal > 0:
        remainder = decimal % base
        rem_stack.push(remainder)
        decimal = decimal // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string


print(base_converter(25, 2))
print(base_converter(31, 16))
