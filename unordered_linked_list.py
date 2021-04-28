class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def get_data(self):
    return self.data

  def get_next(self):
    return self.next

  def set_data(self, new_data):
    self.data = new_data

  def set_next(self, new_next):
    self.next = new_next


class UnorderedList:

  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, data):
    temp = Node(data)
    temp.set_next(self.head)
    self.head = temp

  def size(self):
    current = self.head
    count = 0
    while current is not None:
      count += 1
      current = current.get_next()
    return count

  def search(self, item):
    current = self.head
    found = False
    while current is not None and not found:
      if current.get_data() == item:
        found = True
      else:
        current = current.get_next()

    return found

  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      if current.get_data() == item:
        found = True
      else:
        previous = current
        current = current.get_next()

      if previous == None:
        self.head = current.get_next()
      else:
        previous.set_next(current.get_next())

my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)


print(my_list.size())

print(my_list.search(17))

