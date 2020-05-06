import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 20, 20)
plt.plot(x, 1/x, '--g>', label="f(x) = 1/x")
# plt.axis([1, 20, 0, 1])
plt.ylabel('f(x)')
plt.xlabel('x')
plt.title("Wykres funkcji f(x) = 1/x dla x[1, 20]")
plt.legend()
plt.show()
