import numpy as np
import matplotlib.pylab as plt
from matplotlib import style
style.use('ggplot')
np.random.seed(3)

a = [1,2,5,6,8,3,7,3]
c = [2,2,0,5,4,4,3,2]

def computeQ(a, c, Q0=0):  # initial queue length is 0
    N = len(a)
    Q = np.empty(N, dtype=int)  # make a list to store the values of  Q
    Q[0] = Q0
    for n in range(1, N):
        d = min(Q[n - 1], c[n])
        Q[n] = Q[n - 1] + a[n] - d
    return Q

print(computeQ(a,c))
