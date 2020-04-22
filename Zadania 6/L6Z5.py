import numpy as np


def odw(n):
    return np.diag(np.arange(n, 0, step=-1))


print(odw(3))
print(odw(4))
