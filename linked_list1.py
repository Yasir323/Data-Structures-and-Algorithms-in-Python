# Linked list


class Node():

	def __init__(self, data=0):
		self.data = data
		self.next = None


class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		self.head = None

	# Adding elements to the list
	def append(self, value):
		# If there is no element then make the
		# the first element the 'HEAD'
		if self.head is None:
			self.head = Node(value)
		else:
			current_node = self.head  # Start with the head
			# Iterate if there are more than one elements in the list
			while current_node.next is not None:
				current_node = current_node.next  # Move to next element
			# When we reach the end, add the new value to the end of the list
			current_node.next = Node(value)

	# Method to print the list
	def print_list(self):
		current = self.head
		print('[', end='')
		while current is not None:
			# print(current.data, '->', current.next)
			if current.next == None:
				print(f'{current.data}]')
			else:
				print(f'{current.data},', end=' ')
			current = current.next

	# Method to get the length of the list
	def __len__(self):
		result = 0
		current = self.head
		while current is not None:
			result += 1
			current = current.next
		return result

	# Method for accessing elements using indexing
	def __getitem__(self, key):
		i = 0
		current = self.head
		while current is not None:
			if i == key:
				return current.data
			current = current.next
			i += 1
			if i >= self.__len__():
				raise KeyError ("The list is smaller than the index you have provided")
		return None

	# Method to change the elements using indexing
	def __setitem__(self, key, value):
		i = 0
		current = self.head
		while current is not None:
			if i == key:
				current.data = value
				break
			current = current.next
			i += 1
			if i >= self.__len__():
				raise KeyError ("The list is smaller than the index you have provided")

	# Reversing the linked list
	def reverse(self):
		# Set previous to None
		prev = None
		# Current becomes the first element
		current = self.head
		while current is not None:
			# Store the next element in 'next'
			next = current.next
			# Make current node point towards the previous node
			current.next = prev
			# Move forward in the list
			# Current becomes previous
			prev = current
			# Next becomes current
			current = next
		# At the end, make the last element the 'HEAD'
		self.head = prev


llist = LinkedList()
llist.append(1)
llist.append(3)
llist.append(5)
llist.append(7)
llist.append(9)
llist.append(11)
llist.print_list()
# print(len(llist))
# print(llist[3])
llist[3] = 56
llist.print_list()
llist.reverse()
llist.print_list()