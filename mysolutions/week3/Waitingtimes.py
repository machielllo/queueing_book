import numpy as np
import matplotlib.pylab as plt
from matplotlib import style

np.random.seed(3)

num = 1000
labda = 3
X = np.random.exponential(scale=1/labda, size = num)
#print(sum(X)/100)
X[0] = 0
A = X.cumsum()
#print(len(A), len(X))

mu = 2.8
S = np.random.exponential(scale=1/mu, size=len(A))
S[0] = 0

#print(S.mean())

#D = np.zeros_like(A)
#for k in range(1, len(A)):
#    D[k] = max(D[k-1], A[k]) + S[k]
#
#print("noX0")
#print(D)
#print(A)
#print(S)
#
#D = np.zeros_like(A)
#
#for  k in range(len(A)):
#    try:
#        D[k] = max(D[k-1], A[k]) + S[k]
#    except:
#        D[k] = A[k] + S[k]
#
#print("try/except")
#print(D)
#print(A)
#print(S)

D = np.zeros_like(A)
for k in range(1, len(A)):
    D[k] = max(D[k-1], A[k]) + S[k]

J = D - A
#print(J)
W = J - S
#print(W)

#print(W.mean(), W.std())
#plt.clf()
#plt.plot(J)
#plt.savefig("figures/sojournmu2.8.pdf")

rho = S.sum() / D[-1]
idle = (D[-1] - S.sum()) / D[-1]
print(idle)






