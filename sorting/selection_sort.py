"""
The selection sort algorithm sorts an array by
repeatedly finding the minimum element
(considering ascending order) from unsorted part
and putting it at the beginning.
"""
import numpy as np
import time
from rich import print as rprint
from statistics import fmean


def selectionsort(array):
    size = len(array)
    for i in range(size):
        min_id = i
        for j in range(i + 1, size):
            if array[j] < array[min_id]:
                min_id = j
        array[i], array[min_id] = array[min_id], array[i]


def main():
    array = list(np.random.randint(low=1, high=50, size=10))
    big_array = list(np.random.randint(low=1, high=100000, size=5000))
    rprint("[green]Unsorted array:", array)
    selectionsort(array)
    rprint("[green]Sorted array:", array)
    times = np.array([])
    for i in range(10):
        start_time = time.time()
        selectionsort(big_array)
        stop_time = time.time()
        times = np.append(times, [stop_time - start_time])
    rprint("[yellow]Average Time taken over 10 sorting operations to sort \
    an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
