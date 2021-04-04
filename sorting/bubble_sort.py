"""
Bubble Sort is the simplest sorting algorithm that 
works by repeatedly swapping the adjacent elements 
if they are in wrong order.
"""
import numpy as np
import time
from rich import print as rprint 
import statistics


def bubble_sort(array, size):
	n = size
	for i in range(size):
		for j in range(0, n - i - 1):
			if array[j] > array[j + 1]:
				array[j], array[j + 1] = array[j + 1], array[j]


def main():
	array = np.random.randint(low=1, high=50, size=10)
	size = len(array)
	big_array = np.random.randint(low=1, high=100000, size=5000)
	big_size = len(big_array)
	rprint("[green]Unsorted array:",array)
	bubble_sort(array, size)
	rprint("[green]Sorted array:", array)
	times = np.array([])
	for i in range(10):
		start_time = time.time()
		bubble_sort(big_array, big_size)
		stop_time = time.time()
		times = np.append(times, [stop_time - start_time])
	rprint("[yellow]Average Time taken over 10 sorting operations to sort an array of size 5000:", times.mean(), "[yellow]seconds.")


if __name__ == "__main__":
	main()