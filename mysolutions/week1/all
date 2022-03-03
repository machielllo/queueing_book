import numpy as np
import matplotlib.pyplot as plt
num = 5_000

np.random.seed(3)
a = np.random.randint(5, 9, size=num)
c = (5+8)/1.8 * np.ones(num)
L = np.zeros_like(a, dtype=float)

L[0] = 2_000
for i in range(1, num):
    d = min(c[i], L[i-1])
    L[i] = L[i-1] + a[i] - d


plt.clf()
plt.plot(L)
plt.savefig('queue-discrete_3.pdf')

