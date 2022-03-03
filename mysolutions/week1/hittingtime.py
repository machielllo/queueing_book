import numpy as np

num = 5_000


def hitting_time(seed):
    np.random.seed(seed)
    a = np.random.randint(5, 9, size=num)
    c = (5 + 8) / 1.8 * np.ones(num)
    print(a.mean())
    print(np.mean(a-c))

    L = 2_000
    for i in range(1, num):
        L += +a[i] - c[i]
        if L <= 0:
            return i


N = 100
tau = np.zeros(N)
for n in range(N):
    tau[n] = hitting_time(n)

print(tau.mean(), tau.std())
print(a.mean() - c.mean())

