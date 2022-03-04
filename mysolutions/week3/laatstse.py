import numpy as np

np.random.seed(3)
labda = 3
mu = 4
num = 10
X = np.random.exponential(scale=1 / labda, size=num + 1)
S = np.random.exponential(scale=1 / mu, size=num)
c = np.array([1.0])
W = np.zeros_like(S)
w = np.zeros_like(c)
for k in range(1, len(S)):
    s = w.argmin()
    W[k] = w[s]
    print(w)
    w[s] += S[k] / c[s]
    print(w)
    print(w - X[k + 1])
    w = np.maximum(w - X[k + 1], 0)
    print(w)

print(W)
print(W.mean(), W.std())