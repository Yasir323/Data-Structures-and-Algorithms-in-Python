import random
import time
from statistics import fmean
from rich import print as rprint
import sys

sys.setrecursionlimit(10**6)


def quicksort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        quicksort(array, low, partition_index - 1)
        quicksort(array, partition_index + 1, high)


def partition(array, low, high):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot.
    """
    pivot = array[high]
    i = low - 1
    j = low
    while j < high:

        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

        j += 1
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1



def main():
    random.seed(42)
    array = [random.randint(a=1, b=50) for _ in range(10)]
    size = len(array)
    big_array = [random.randint(a=1, b=100000) for _ in range(5000)]
    big_size = len(big_array)
    rprint("[green]Unsorted array:",array)
    quicksort(array, 0, size - 1)
    rprint("[green]Sorted array:", array)
    times = []
    for i in range(10):
        start_time = time.time()
        quicksort(big_array, 0, big_size - 1)
        stop_time = time.time()
        times.append(stop_time - start_time)
    rprint("[yellow]Average Time taken over 10 sorting operations to sort an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
