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


class OrderedList:
  def __init__(self):
    self.head = None

  def is_empty(self):
    return self.head == None

  def add(self, data):
    current = self.head
    previous = None
    stop = False
    # Find the correct position to put the item
    while current is not None and not stop:
      if current.get_data() > item:
        stop = True
      else:
        previous = current
        current = current.get_next()
    # Make a temp node
    temp = Node(item)
    # Check if the item has to be placed at first position
    if previous == None:
      # Make item the head of the list
      temp.set_next(self.head)
      self.head = temp
    # Otherwise
    else:
      # Current becomes next of temp
      temp.set_next(current)
      # And temp becomes next of previous
      previous.set_next(temp)

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
    stop = False
    while current is not None and not found and not stop:
      if current.get_data() == item:
        found = True
      else:
        if current.get_data() > item:
          stop = True
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

