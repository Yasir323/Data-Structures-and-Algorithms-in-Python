import numpy as np
import time
from rich import print as rprint 


def search(array, left, right, query):
	mid = left + (right - left) // 2
	if right >= left:
		if array[mid] == query:
			return mid

		elif array[mid] > query:
			return search(array, left, mid - 1, query)

		else:
			return search(array, mid + 1, right, query)

	else:
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