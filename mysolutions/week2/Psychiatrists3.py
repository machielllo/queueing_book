import numpy as np
import matplotlib.pylab as plt
from matplotlib import style
style.use('ggplot')
np.random.seed(3)

def computeQ(a, c, Q0=0):  # initial queue length is 0
    N = len(a)
    Q = np.empty(N, dtype=int)  # make a list to store the values of  Q
    work = np.empty(N-1, dtype=int)      
    Q[0] = Q0
    for n in range(1, N):
        d = min(Q[n - 1], c[n])
        Q[n] = Q[n - 1] + a[n] - d
        work[n-1] = d
    return Q, work

def computeQExtra(a, c, e, Q0=0):  #  initial queue length is 0
    N = len(a)
    Q = [0] * N  # make a list to store the values of  Q
    work = np.empty(N-1, dtype=int) 
    Q[0] = Q0
    for n in range(1, N):
        if Q[n - 1] < lower_thres:
            C = c - e
        elif Q[n-1] >= upper_thres:
            C = c + e
        else:
            C = c
        d = min(Q[n-1], C)
        Q[n] = Q[n-1] + a[n] -d
        work[n-1] = d
    return Q, work

lower_thres = 10
upper_thres = 14

a = np.random.poisson(11.8, 1000)
c = 12

Q = computeQ(a, c * np.ones_like(a))
Qe1 = computeQExtra(a, c, 2)
#Qe5 = computeQExtra(a, c, 5)

#print(Q[1].mean(), Qe1[1].mean(), Qe5[1].mean())

plt.clf()
plt.plot(Q[0], label="Q", color='black')
plt.plot(Qe1[0], label="Qe1", color='green')
#plt.plot(Qe5[0], label="Qe5", color='red')

plt.savefig("plots/psychmyfinal.pdf")

