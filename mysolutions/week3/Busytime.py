import numpy as np

np.set_printoptions(suppress=True)
np.random.seed(3)
num = 15
labda = 3
X = np.random.exponential(scale=1 / labda, size=num)
X[0] = 0
A = X.cumsum()
mu = 1.2 * labda
S = np.random.exponential(scale=1 / mu, size=len(A))
S[0] = 0
D = np.zeros_like(A)
for k in range(1, len(A)):
    D[k] = max(D[k - 1], A[k]) + S[k]

W = D - S - A  # waiting times
idx = np.argwhere(np.isclose(W, 0))
idx = idx[1:]
idle_times = np.maximum(A[idx] - D[idx - 1], 0)
print(idle_times.sum())
print(idx)
busy_times = D[idx - 1][1:] - A[idx][:-1]

last_busy = D[-1] - A[idx[-1]]
print(busy_times.sum() + last_busy, S.sum())
