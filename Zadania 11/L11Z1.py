import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.linspace(0, 2*np.pi, 100)
z = t
x = np.sin(t)
y = np.cos(t)*2
ax.plot(x, y, z, label='Zadanie 1')
ax.legend()
plt.show()
