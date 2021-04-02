import numpy as np
import time
from rich import print as rprint 
from binary_search import search as binary_search


def exponential_search(array, size, x):
	if array[0] == x:
		return 0

	i = 1
	while i < size and array[i] <= x:
		i *= 2

	return binary_search(array, i // 2, min(i, size-1), x)


def main():
	array = np.arange(1, 9999999, 1)
	query = np.random.randint(1, 9999999)
	size = len(array)
	start_time = time.time()
	result = exponential_search(array, size, query)
	stop_time = time.time()
	if result == -1:
		rprint("[red]Element {} is not present in the array.".format(query))
	else:
		rprint("[green]ELement[/green] {} [green]found in the array at index:[/green] {}".format(query, result))
	rprint("[yellow]Total time taken:", stop_time - start_time, "[yellow]seconds.")


if __name__ == "__main__":
	main()