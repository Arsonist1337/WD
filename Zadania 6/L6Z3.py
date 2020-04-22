import numpy as np


def tablica(n):
    return np.arange(1, n * n + 1).reshape((n, n))


print(tablica(2))
