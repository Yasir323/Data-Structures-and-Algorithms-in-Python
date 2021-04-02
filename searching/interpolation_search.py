import numpy as np
import time
from rich import print as rprint 

"""
The Interpolation Search is an improvement over 
Binary Search for instances, where the values in 
a sorted array are uniformly distributed. Binary 
Search always goes to the middle element to check. 
On the other hand, interpolation search may go to 
different locations according to the value of the 
key being searched. For example, if the value of 
the key is closer to the last element, interpolation 
search is likely to start search toward the end side.

pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])
"""


def search(array, lo, hi, x):
	pos = lo + (hi - lo) // 2
	if (lo <= hi and x >= array[lo] and x <= array[hi]):
		
		pos = lo + (x - array[lo]) *(hi - lo) // (array[hi] - array[lo])
		if array[pos] == x:
			return pos

		elif array[pos] > x:
			return search(array, lo, pos - 1, x)

		else:
			return search(array, pos + 1, hi, x)

	else:
		return -1


def main():
	array = np.arange(1, 9999999, 1)
	query = np.random.randint(1, 9999999)
	size = len(array)
	start_time = time.time()
	result = search(array=array, lo=0, hi=size - 1, x=query)
	stop_time = time.time()
	if result == -1:
		rprint("[red]Element {} is not present in the array.".format(query))
	else:
		rprint("[green]ELement[/green] {} [green]found in the array at index:[/green] {}".format(query, result))
	rprint("[yellow]Total time taken:", stop_time - start_time, "[yellow]seconds.")


if __name__ == "__main__":
	main()