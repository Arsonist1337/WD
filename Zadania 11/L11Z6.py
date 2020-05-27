import matplotlib.pyplot as plt
import numpy as np

ax = plt.subplot(121, projection='3d')
X = 100*np.random.rand(20)
Y = 100*np.random.rand(20)
Z = 100*np.random.rand(20)
ax.scatter(X, Y, Z, c='g')

ax2 = plt.subplot(122, projection='3d')
X = 100*np.random.rand(5)
Y = 100*np.random.rand(5)
Z = 100*np.random.rand(5)
ax2.plot(X, Y, Z, c='y')

plt.show()
