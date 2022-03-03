import matplotlib.pyplot as plt
import numpy as np

num = 5_000

np.random.seed(3)
a = np.random.randint(5, 9, size=num)
c = (5+8)/2.3 * np.ones(num)
L = np.zeros_like(a, dtype=float)

L[0] = 20
for i in range(1, num):
    d = min(c[i], L[i-1])
    L[i] = L[i-1] + a[i] - d


plt.clf()
plt.plot(L)
plt.savefig('queue-discrete_2.pdf')

