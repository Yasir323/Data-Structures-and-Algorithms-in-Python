"""
Merge Sort is a Divide and Conquer algorithm. It
divides the input array into two halves, calls
itself for the two halves, and then merges the two
sorted halves. The merge() function is used for
merging two halves. The merge(arr, l, m, r) is a
key process that assumes that arr[l..m] and
arr[m+1..r] are sorted and merges the two sorted
sub-arrays into one.
"""
import numpy as np
import time
from rich import print as rprint
from statistics import fmean
import sys

sys.setrecursionlimit(10 ** 6)


def mergesort(array):
    if len(array) > 1:

        # Finding the mid of the array
        mid = len(array)//2

        # Dividing the array elements
        L = array[:mid]

        # into 2 halves
        R = array[mid:]

        # Sorting the first half
        mergesort(L)

        # Sorting the second half
        mergesort(R)

        i = j = k = 0

        # Copy data to temp arrayays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


def main():
    array = list(np.random.randint(low=1, high=50, size=10))
    big_array = list(np.random.randint(low=1, high=100000, size=5000))
    rprint("[green]Unsorted array:", array)
    mergesort(array)
    rprint("[green]Sorted array:", array)
    times = np.array([])
    for i in range(10):
        start_time = time.time()
        mergesort(big_array)
        stop_time = time.time()
        times = np.append(times, [stop_time - start_time])
    rprint("[yellow]Average Time taken over 10 sorting operations to sort \
an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
