import numpy as np

a = np.zeros((100), dtype=str).reshape(10, 10)
a.fill(' ')
a[np.random.randint(0, a.shape[0]), 1:7] = np.frombuffer(b'ananas', dtype='S1')
a[4:10, np.random.randint(0, a.shape[1])] = np.frombuffer(b'bazant', dtype='S1')
np.put(a, [1, 12, 23, 34, 45, 56], np.array(list('muzyka'), dtype=str))
print(a)
