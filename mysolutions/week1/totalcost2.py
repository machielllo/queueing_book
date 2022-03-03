import numpy as np

np.random.seed(2)

num = 50

a = np.random.randint(5, 9, size=num)
c = 7 * np.ones(num)
L = np.zeros_like(a)
R = np.zeros_like(a)
beta = 1.2
h = 2

L[0] = 10
for k in range(1, num):
    d = min(c[k], L[k-1] + a[k])
    L[k] = L[k-1] + a[k] - d
    R[k] = beta * c[k] + h*L[k] 

print(sum(R))
