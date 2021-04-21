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
import sys

sys.setrecursionlimit(10**6)


def countsort(array, exp):
	n = len(array)
	output = [0] * size
	count = [0] * 10
	for i in range(n):
		


def radixsort(array):
	# Find the maximum number to know ti=he number of digits
	max1 = max(array)
	# Use count sort for every digit. Note that instead of
	# passing digit number, exp is passed. exp is 10^i
	# where i is the current digit place
	exp = 1
	while max1 / exp > 0:
		countsort(array, exp)
		exp += 10


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
