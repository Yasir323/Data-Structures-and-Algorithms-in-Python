"""
Bubble Sort is the simplest sorting algorithm that
works by repeatedly swapping the adjacent elements
if they are in wrong order.
"""
import numpy as np
import time
from rich import print as rprint
from statistics import fmean


def bubblesort(array):
    size = len(array)
    n = size
    for i in range(size):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    array = list(np.random.randint(low=1, high=50, size=10))
    big_array = list(np.random.randint(low=1, high=100000, size=5000))
    rprint("[green]Unsorted array:", array)
    bubblesort(array)
    rprint("[green]Sorted array:", array)
    times = np.array([])
    for i in range(10):
        start_time = time.time()
        bubblesort(big_array)
        stop_time = time.time()
        times = np.append(times, [stop_time - start_time])
    rprint("[yellow]Average Time taken over 10 sorting operations to sort an \
array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
