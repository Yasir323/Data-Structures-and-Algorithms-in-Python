import numpy as np
import time
from rich import print as rprint 


def search(array, size, x):
	for i in range(0, size):
		if array[i] == x:
			return i
	return -1


def main():
	array = np.random.randint(low=1, high=1000000, size=9999999)
	li = list(array)
	query = 786
	size = len(array)

	start_time = time.time()
	result = search(li, size, query)
	stop_time = time.time()
	if result == -1:
		rprint("[red]Element is not present in the array.")
	else:
		rprint("[green]ELement found in the array at index:",result)
	rprint("[yellow]Total time taken to search a list:", stop_time - start_time, "[yellow]seconds.")


	start_time = time.time()
	result = search(array, size, query)
	stop_time = time.time()
	if result == -1:
		rprint("[red]Element is not present in the array.")
	else:
		rprint("[green]ELement found in the array at index:",result)
	rprint("[yellow]Total time taken to search a numpy array:", stop_time - start_time, "[yellow]seconds.")

if __name__ == "__main__":
	main()