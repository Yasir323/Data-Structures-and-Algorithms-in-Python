class Deque:

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)


def pal_checker(str):
    deque = Deque(list(str))
    is_pallindrome = True
    while len(deque) > 1 and is_pallindrome:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            is_pallindrome = False

    return is_pallindrome


print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))
