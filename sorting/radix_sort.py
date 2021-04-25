"""
Counting sort is a linear time sorting algorithm that
sort in O(n+k) time when elements are in the range
from 1 to k.

What if the elements are in the range from 1 to n2?
We can’t use counting sort because counting sort will
take O(n2) which is worse than comparison-based
sorting algorithms. Can we sort such an array in
linear time?

Radix Sort is the answer. The idea of Radix Sort is
to do digit by digit sort starting from least
significant digit to most significant digit. Radix
sort uses counting sort as a subroutine to sort.

Let there be d digits in input integers. Radix Sort
takes O(d*(n+b)) time where b is the base for
representing numbers, for example, for the decimal
system, b is 10.
"""
import random
import time
from statistics import fmean
from rich import print as rprint
# import sys

# sys.setrecursionlimit(10**6)


def countsort(array, exp):
    n = len(array)
    output = [0] * n
    count = [0] * 10
    # Store count of occurences in count
    for i in range(n):
        index = int(array[i] / exp)
        count[index % 10] += 1
    # Change count so that count now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = int(array[i] / exp)
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        array[i] = output[i]


def radixsort(array):
    # Find the maximum number to know ti=he number of digits
    max1 = max(array)
    # Use count sort for every digit. Note that instead of
    # passing digit number, exp is passed. exp is 10^i
    # where i is the current digit place
    exp = 1
    while max1 / exp > 0:
        countsort(array, exp)
        exp *= 10


def main():
    random.seed(42)
    array = [random.randint(a=1, b=50) for _ in range(10)]
    big_array = [random.randint(a=1, b=100000) for _ in range(5000)]
    rprint("[green]Unsorted array:", array)
    radixsort(array)
    rprint("[green]Sorted array:", array)
    times = []
    for i in range(10):
        start_time = time.time()
        radixsort(big_array)
        stop_time = time.time()
        times.append(stop_time - start_time)
    rprint("[yellow]Average Time taken over 10 sorting operations to \
    sort an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
