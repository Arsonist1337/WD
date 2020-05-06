import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(0, 30, 0.1)
s = [-math.sin(y) + 2 for y in x]
c = np.sin(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='sin(x)')
plt.ylabel('sin(x)')
plt.xlabel('x')
plt.title("Wykres funkcji sin(x) zmodyfikowany")
plt.legend()
plt.show()
