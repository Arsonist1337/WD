import numpy as np


def potega(n, m):
    return np.logspace(1, m, base=n, num=m, dtype='int')


print(potega(2, 4))
print(potega(3, 4))
print(potega(4, 6))
