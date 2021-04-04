import numpy as np


def power_dac(x, y):
	if (y == 0): return 1
	elif int(y % 2) == 0:
		return power_dac(x, y // 2) * power_dac(x, y // 2)

	else:
		return x * power_dac(x, y // 2) * power_dac(x, y // 2)


x = np.random.randint(1, 100); y = np.random.randint(1, 10)
print(f'{x} raised to the power of {y} = {power_dac(x, y)}')