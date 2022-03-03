import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)

num = 5000

np.random.seed(3)
a = np.random.randint(0, 100, size=num)
c = 5 * np.ones(num)
L = np.zeros_like(a)

K = 30
p = np.zeros(K + 1)

L[0] = 28
for i in range(1, num):
    d = min(c[i], L[i - 1])
    L[i] = min(L[i - 1] + a[i] - d, K)
    p[L[i]] += 1

p /= p.sum()
plt.clf()
plt.plot(p)
plt.savefig('queue-discrete-loss-p.pdf')
print(p)
print(a.sum()/c.sum())
