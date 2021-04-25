# Program to check for closing paranthesis


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


def par_checker(string):
    stack = Stack()
    balanced = True
    for char in string:
        if char == "(":
            stack.push(char)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()

    if balanced and stack.is_empty():
        return True

    else:
        return False


print(par_checker('((()))'))  # True
print(par_checker('(()'))  # False
