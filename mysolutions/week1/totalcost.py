import numpy as np

np.random.seed(2)

num = 50

a = np.random.randint(5, 9, size=num)
c = 7* np.ones(num)
L = np.zeros_like(a)
R = np.zeros_like(a)
Check = np.zeros_like(a)
beta = 1.2
h = 2

L[0] = 10
Check[0] = 10
for k in range(1, num):
    L_R = max(L[k-1] - c[k], 0)
    c_R = max(c[k] - L[k-1], 0)
    d = min(c_R, L_R + a[k])
    a_R = max(a[k] - c_R, 0)
    L[k] = L_R + a[k] - d
    Check[k] = L_R + a_R
    R[k] = beta * c[k] + h *(L_R + a_R)

print(mean(L == Check))
print(sum(R))
