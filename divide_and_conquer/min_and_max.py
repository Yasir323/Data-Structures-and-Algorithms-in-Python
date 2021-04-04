import numpy as np
import time
from rich import print as rprint 


def dac_max(array, index, size):
	max_num = -1
	if index >= size - 2:
		if array[index] > array[index + 1]:
			return array[index]
		else:
			return array[index + 1]

	max_num = dac_max(array, index + 1, size)

	if array[index] > max_num:
		return array[index]
	else:
		return max_num


def dac_min(array, index, size):
	min_num = -1
	if index >= size - 2:
		if array[index] < array[index + 1]:
			return array[index]
		else:
			return array[index + 1]

	min_num = dac_min(array, index + 1, size)

	if array[index] < min_num:
		return array[index]
	else:
		return min_num


def main():
	array = np.random.randint(low=1, high=1000000, size=99)
	size = len(array)
	rprint(max(array) == dac_max(array, 0, size))
	rprint(min(array) == dac_min(array, 0, size))

if __name__ == "__main__":
	main()