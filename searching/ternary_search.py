"""
In Ternary Search we divide 3 times on every iteration.
It might be better than BInary Search in some cases, but
in worst case scenario it involves more comparisons than
Binary Search and that is why the latter one is preferred.

Time Complexity for Binary search = 2clog2n + O(1)
Time Complexity for Ternary search = 4clog3n + O(1)

The following is recursive formula for counting 
comparisons in worst case of Binary Search.

   T(n) = T(n/2) + 2,  T(1) = 1

The following is recursive formula for counting 
comparisons in worst case of Ternary Search.

   T(n) = T(n/3) + 4, T(1) = 1
"""
import numpy as np
import time
from rich import print as rprint 


def search(array, left, right, query):
	if right >= left:
		mid1 = left + (right - left) // 3
		mid2 = mid1 + (right - left) // 3
		if array[mid1] == query:
			return mid1

		if array[mid2] == query:
			return mid2

		if array[mid1] > query:
			return search(array, left, mid1 - 1, query)

		if array[mid2] < query:
			return search(array, mid2 + 1, right, query)

		return search(array, mid1 + 1, mid2 - 1, query)	
	return -1


def main():
	array = np.arange(1, 9999999, 1)
	query = np.random.randint(1, 9999999)
	size = len(array)
	start_time = time.time()
	result = search(array=array, left=0, right=size - 1, query=query)
	stop_time = time.time()
	if result == -1:
		rprint("[red]Element {} is not present in the array.".format(query))
	else:
		rprint("[green]ELement[/green] {} [green]found in the array at index:[/green] {}".format(query, result))
	rprint("[yellow]Total time taken:", stop_time - start_time, "[yellow]seconds.")


if __name__ == "__main__":
	main()