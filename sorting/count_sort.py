"""
Counting sort is a sorting technique based on keys 
between a specific range. It works by counting the 
number of objects having distinct key values (kind 
of hashing). Then doing some arithmetic to calculate
the position of each object in the output sequence.

Time Complexity: O(n+k) where n is the number of 
elements in input array and k is the range of input. 
Auxiliary Space: O(n+k)
"""
import random
import time
from statistics import fmean
from rich import print as rprint
# import sys

# sys.setrecursionlimit(10**6)


def countsort(array):
    max_element = int(max(array))
    min_element = int(min(array))
    array_range = max_element - min_element + 1
    size = len(array)
    # Create a count array to store the count of individual
    # elements and initialize count array as 0
    count = [0] * array_range
    output = [0] * size

    # Store the counter for each character
    for i in range(size):
        count[array[i] - min_element] += 1

    # Change count[i] so that count[i] 
    # now contains actual position of this element
    # in output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(size - 1, -1, -1):
        output[count[array[i] - min_element] - 1] = array[i]
        count[array[i] - min_element] -= 1
    
    # Copy the output array to array so that array now
    # contains the sorted array
    for i in range(size):
        array[i] = output[i]

    return array    


def main():
    random.seed(42)
    array = [random.randint(a=1, b=50) for _ in range(10)]
    # size = len(array)
    big_array = [random.randint(a=1, b=100000) for _ in range(5000)]
    # big_size = len(big_array)
    rprint("[green]Unsorted array:",array)
    countsort(array)
    rprint("[green]Sorted array:", array)
    times = []
    for i in range(10):
        start_time = time.time()
        countsort(big_array)
        stop_time = time.time()
        times.append(stop_time - start_time)
    rprint("[yellow]Average Time taken over 10 sorting operations to sort an array of size 5000:", fmean(times), "[yellow]seconds.")


if __name__ == "__main__":
    main()
