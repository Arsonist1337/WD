import numpy as np


def funkcja(tab, kierunek):
    s = tab.shape
    x = s[0]
    y = s[1]
    n = 0
    m = 0

    if kierunek == 0 and x % 2 != 0:
        return print("Ilośc wierszy nie pozwala na operacje")

    if kierunek == 0:
        n = tab[:int(x/2)]
        m = tab[int(x/2):int(x)]

    if kierunek == 0 and y % 2 != 0:
        return print("Ilośc kolumn nie pozwala na operacje")

    if kierunek == 1:
        n = tab[:, :int(y/2)]
        m = tab[:, int(y/2):int(y)]

    else 
        return tab % kierunek
    print(n)
    print(m)


tab = np.arange(16).reshape((4, 4))
print(tab)
print(funkcja(tab, 2))
