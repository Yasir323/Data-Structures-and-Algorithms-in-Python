import numpy as np
import time
from rich import print as rprint
from statistics import fmean


def short_bubble_sort(array):
    size = len(array)
    n = size - 1
    swap = True
    while n > 0 and swap:
        swap = False
        for j in range(n):
            if array[j] > array[j + 1]:
                swap = True
                array[j], array[j + 1] = array[j + 1], array[j]
        n -= 1


def main():
    array = list(np.random.randint(low=1, high=50, size=10))
    big_array = list(np.random.randint(low=1, high=100000, size=5000))
    rprint("[green]Unsorted array:", array)
    short_bubble_sort(array)
    rprint("[green]Sorted array:", array)
    times = np.array([])
    for i in range(10):
        start_time = time.time()
        short_bubble_sort(big_array)
        stop_time = time.time()
        times = np.append(times, [stop_time - start_time])
    rprint("[yellow]Average Time taken over 10 sorting operations to sort an \
array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
