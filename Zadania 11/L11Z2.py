import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)


def randrange(n, vmin, vmax):
    '''
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -50, -5),
                          ('purple', 'd', -30, -5), ('y', '+', -10, -15),
                          ('g', '3', -25, -10)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
