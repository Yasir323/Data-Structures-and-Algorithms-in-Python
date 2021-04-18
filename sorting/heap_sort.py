"""
Heap sort is a comparison based sorting technique 
based on Binary Heap data structure. It is similar to
selection sort where we first find the minimum
element and place the minimum element at the
beginning.

A Binary Heap is a Complete Binary Tree where items
are stored in a special order such that value in a
parent node is greater(or smaller) than the values in
its two children nodes. The former is called as max
heap and the latter is called min-heap. The heap can
be represented by a binary tree or array.
"""
import random
import time
from statistics import fmean
from rich import print as rprint


def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1  # left = 2i+1
	r = 2 * i + 2  # right = 2i+2

	# See if the left child of root exists and is greater than root
	if l < n and arr[largest] < arr[l]:
		largest = l

	# Same for the right child
	if r < n and arr[largest] < arr[r]:
		largest = r

	# Change root if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		# Heapify the root
		heapify(arr, n, largest)


def heap_sort(arr, n):
	n = len(arr)

	# Build a max heap
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)

	# One by one extract elements
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # Swap
		heapify(arr, i, 0)


def main():
	random.seed(42)
	array = [random.randint(a=1, b=50) for _ in range(10)]
	size = len(array)
	big_array = [random.randint(a=1, b=100000) for _ in range(5000)]
	big_size = len(big_array)
	rprint("[green]Unsorted array:",array)
	heap_sort(array, size)
	rprint("[green]Sorted array:", array)
	times = []
	for i in range(10):
		start_time = time.time()
		heap_sort(big_array, big_size)
		stop_time = time.time()
		times.append(stop_time - start_time)
	rprint("[yellow]Average Time taken over 10 sorting operations to sort an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
	main()