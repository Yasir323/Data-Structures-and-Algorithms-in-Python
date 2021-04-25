class Queue():

    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return self.items == []

    def enqueue(self, items):
        self.items.insert(0, items)

    def dequeue(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


def hot_potato(name_list, num):
    queue = Queue()
    # Populate the queue first
    for name in name_list:
        queue.enqueue(name)

    while len(queue) > 1:
        for i in range(num):
            # Rotate the queue num number of times
            queue.enqueue(queue.dequeue())
        # Then remove the last element
        queue.dequeue()

    return queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
