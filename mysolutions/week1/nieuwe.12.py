import numpy as np
import matplotlib.pyplot as plt

num = 500
L0 = 100


def hitting_time():
        a = np.random.randint(5, 10, size=num)
        c = (5 + 9) / 1.2 * np.ones(num)
        a[0] = L0
        Z = (a - c).cumsum()
        plt.plot(Z)
        return


samples = 30
for n in range(samples):
    hitting_time()

plt.savefig("free-random-walk1.2.pdf")

