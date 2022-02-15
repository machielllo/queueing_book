import numpy as np
import matplotlib.pyplot as plt
num = 500

np.random.seed(3)
a = np.random.randint(0, 20, size=num)
c = 10*np.ones(num)
L = np.zeros_like(a)
loss = np.zeros_like(a)

K = 30 # max people in queue, otherwise they leave

L[0] = 28
for i in range(1, num):
    d = min(c[i], L[i-1])
    loss[i] = max(L[i-1] + a[i] - K, 0)  # this
    L[i] = L[i-1] + a[i] - d - loss[i] # this 2

lost_fraction = sum(loss)/sum(a)
print(lost_fraction)

plt.clf()
plt.plot(L)
plt.savefig('queue-discrete-after.pdf')

