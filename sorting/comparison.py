import random
import time
from rich import print as rprint
import sys
from bubble_sort import bubblesort
from count_sort import countsort
from heap_sort import heapsort
from insertion_sort import insertionsort
from merge_sort import mergesort
from quick_sort2 import quicksort
from radix_sort import radixsort
from selection_sort import selectionsort

sys.setrecursionlimit(10**6)


def main():
    sorting_algorithms = {
        "Bubble Sort": bubblesort,
        "Count Sort": countsort,
        "Heap Sort": heapsort,
        "Insertion Sort": insertionsort,
        "Merge Sort": mergesort,
        "Quick Sort": quicksort,
        "Radix Sort": radixsort,
        "Selection Sort": selectionsort,
    }
    ls = list(sorting_algorithms.keys())
    times = {}
    for algorithm in ls:
        random.seed(42)
        array = list(random.randint(a=1, b=100000) for _ in range(5000))
        size = len(array)
        # rprint("[green]Unsorted array:", array)
        start_time = time.time()
        if algorithm == "Quick Sort":
            quicksort(array, 0, size - 1)
        else:
            sorting_algorithms[algorithm](array)
        stop_time = time.time()
        # rprint("[green]Sorted array:", array)
        time_taken = stop_time - start_time
        times[algorithm] = time_taken
        rprint("[yellow]Time taken to sort an array of size 5000 using", algorithm, ":", time_taken, "[yellow]seconds.")
    least_time = min(list(times.values()))
    highest_time = max(list(times.values()))
    fastest_algorithm = list(times.keys())[list(times.values()).index(least_time)]
    slowest_algorithm = list(times.keys())[list(times.values()).index(highest_time)]
    rprint("[yellow]The fastest algorithm is:", fastest_algorithm)
    rprint("[yellow]The slowest algorithm is:", slowest_algorithm)


if __name__ == "__main__":
    main()
