import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(111, projection='3d')
X = 100*np.random.rand(20)
Y = 100*np.random.rand(20)
Z = 100*np.random.rand(20)
ax.scatter(X, Y, Z, c='r', label='Jabłka')

X = 100*np.random.rand(5)
Y = 100*np.random.rand(5)
Z = 100*np.random.rand(5)
ax.plot(X, Y, Z, c='g', label='Wąż')

plt.legend()
plt.title("Snake w 3D", c='b')
plt.show()
