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
from statistics import fmean


def insertionsort(array):
    size = len(array)
    for i in range(1, size):
        j = i
        while j > 0:
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


def main():
    array = list(np.random.randint(low=1, high=50, size=10))
    big_array = list(np.random.randint(low=1, high=100000, size=5000))
    rprint("[green]Unsorted array:", array)
    insertionsort(array)
    rprint("[green]Sorted array:", array)
    times = np.array([])
    for i in range(10):
        start_time = time.time()
        insertionsort(big_array)
        stop_time = time.time()
        times = np.append(times, [stop_time - start_time])
    rprint("[yellow]Average Time taken over 10 sorting operations to sort \
an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
