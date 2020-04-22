import numpy as np


def funkcja(n):
    for a in range(n):
        a = np.zeros(n*n).reshape(n, n)
        a = a + np.diag([2, 2, 2])
        a = a + np.diag([4, 4], 1)
        a = a + np.diag([4, 4], -1)
        a = a + np.diag([6], 2)
        a = a + np.diag([6], -2)
    return a


macierz = funkcja(3)
print(macierz)
