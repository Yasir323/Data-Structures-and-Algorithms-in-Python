"""
Insertion sort is a simple sorting algorithm that 
works similar to the way you sort playing cards in 
your hands. The array is virtually split into a 
sorted and an unsorted part. Values from the unsorted 
part are picked and placed at the correct position 
in the sorted part.
"""
import numpy as np
import time
from rich import print as rprint 


def selection_sort(array, size):
	for i in range(1, size):
		j = i
		while j > 0:
			if array[j] < array[j - 1]:
				array[j], array[j - 1]	= array[j - 1], array[j]
			j -= 1


def main():
	array = np.random.randint(low=1, high=50, size=10)
	size = len(array)
	big_array = np.random.randint(low=1, high=100000, size=5000)
	big_size = len(big_array)
	rprint("[green]Unsorted array:",array)
	selection_sort(array, size)
	rprint("[green]Sorted array:", array)
	times = np.array([])
	for i in range(10):
		start_time = time.time()
		selection_sort(big_array, big_size)
		stop_time = time.time()
		times = np.append(times, [stop_time - start_time])
	rprint("[yellow]Average Time taken over 10 sorting operations to sort an array of size 5000:", times.mean(), "[yellow]seconds.")


if __name__ == "__main__":
	main()