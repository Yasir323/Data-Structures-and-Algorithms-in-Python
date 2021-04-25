# Program to check closing of all brackets


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


def matches(open, close):
    opens = '[{('
    closers = ']})'
    return opens.index(open) == closers.index(close)


def par_checker(str):
    stack = Stack()
    balanced = True
    for char in str:
        if char in "([{":
            stack.push(char)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not matches(top, char):
                    balanced = False

    if balanced and stack.is_empty():
        return True

    else:
        return False


print(par_checker('{({([][])}())}'))  # True
print(par_checker('[{()]'))  # False
