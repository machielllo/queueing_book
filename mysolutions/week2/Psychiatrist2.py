import numpy as np
import matplotlib.pylab as plt
from matplotlib import style
style.use('ggplot')
np.random.seed(3)

def unbalanced(a):
    p = np.empty([5, len(a)])
    p[0, :] = 1.0 * np.ones_like(a)
    p[1, :] = 1.0 * np.ones_like(a)
    p[2, :] = 1.0 * np.ones_like(a)
    p[3, :] = 3.0 * np.ones_like(a)
    p[4, :] = 9.0 * np.ones_like(a)
    return p

def balanced(a):
    p = np.empty([5, len(a)])
    p[0, :] = 2.0 * np.ones_like(a)
    p[1, :] = 2.0 * np.ones_like(a)
    p[2, :] = 3.0 * np.ones_like(a)
    p[3, :] = 4.0 * np.ones_like(a)
    p[4, :] = 4.0 * np.ones_like(a)
    return p

def balanced2(a):
    p = np.empty([5, len(a)])
    p[0, :] = 3.0 * np.ones_like(a)
    p[1, :] = 3.0 * np.ones_like(a)
    p[2, :] = 3.0 * np.ones_like(a)
    p[3, :] = 3.0 * np.ones_like(a)
    p[4, :] = 3.0 * np.ones_like(a)
    return p

def unbalanced2(a):
    p = np.empty([5, len(a)])
    p[0, :] = 0 * np.ones_like(a)
    p[1, :] = 0 * np.ones_like(a)
    p[2, :] = 0 * np.ones_like(a)
    p[3, :] = 0 * np.ones_like(a)
    p[4, :] = 15 * np.ones_like(a)
    return p

def balanced3(a):
    p = np.empty([5, len(a)])
    p[0, :] = 2 * np.ones_like(a)
    p[1, :] = 2 * np.ones_like(a)
    p[2, :] = 3.2 * np.ones_like(a)
    p[3, :] = 3.2 * np.ones_like(a)
    p[4, :] = 4 * np.ones_like(a)
    return p

def spread_holidays(p):
    for j in range(len(a)):
        psych = j % 5
        p[psych, j] = 0

def synchronize_holidays(p):
    for j in range(int(len(a) / 5)):
        p[:, 5 * j] = 0  # this

def synchronize_holidays6(p):
    for j in range(int(len(a) / 6)):
        p[:, 6 * j] = 0  # this

def weird_holiday_idea(p):
    for j in range(np.shape(p)[0]):
        work = np.random.poisson(5, int(len(a)/5))
        x = 0
        for i in work:
            x = min(i+x, 999)
            p[j,x] = 0


def computeQ(a, c, Q0=0):  # initial queue length is 0
    N = len(a)
    Q = np.empty(N, dtype=int)  # make a list to store the values of  Q
    Q[0] = Q0
    for n in range(1, N):
        d = min(Q[n - 1], c[n])
        Q[n] = Q[n - 1] + a[n] - d
    return Q

def computeQExtra(a, c, e, Q0=0):  #  initial queue length is 0
    N = len(a)
    Q = np.empty(N, dtype=int)   # make a list to store the values of  Q
    work = np.empty(N-1, dtype=int) 
    Q[0] = Q0
    count = 0
    for n in range(1, N):
        try:
            counter = C
        except:
            pass
        if Q[n - 1] < lower_thres:
            C = c[n] - e
        elif Q[n-1] >= upper_thres:
            C = c[n] + e
        else:
            C = c[n]
        try:
            if C != counter:
                count += 1
        except:
            pass
        d = min(Q[n-1], C)
        Q[n] = Q[n-1] + a[n] -d
        work[n-1] = d
    return Q, work, count

lower_thres = 14
upper_thres = 18

a = np.random.poisson(11.8, 1000)
p = unbalanced(a)
spread_holidays(p)
s = np.sum(p, axis=0)
#Q = computeQ(a, s)

Qe1 = computeQExtra(a, s, 3)
print(Qe1[2])

lower_thres = 14
upper_thres = 34

Qe5 = computeQExtra(a, s, 6)
print(Qe5[2])

plt.clf()
plt.plot(Qe1[0], label="Qe1", color='orange')
plt.plot(Qe5[0], label="Qe5", color='grey')
plt.savefig("plots/psychmyfinal.pdf")

#ubp = unbalanced(a)
#spread_holidays(ubp)
#s = np.sum(ubp, axis=0)

#plt.clf()
#Q1 = computeQ(a,s)
#plt.plot(Q1)
#plt.savefig("plots/psych1.pdf")

#bp = balanced(a)
#spread_holidays(bp)
#s = np.sum(bp, axis=0)

#Q2 = computeQ(a,s)
#plt.plot(Q2)
#plt.savefig("plots/psych2.pdf")

#ubp2 = unbalanced2(a)
#spread_holidays(ubp2)
#s = np.sum(ubp2, axis=0)

#plt.clf()

#Q3 = computeQ(a,s)
#plt.plot(Q3)

#bp2 = balanced2(a)
#spread_holidays(bp2)
#s = np.sum(bp2, axis=0)

#Q4 = computeQ(a,s)
#plt.plot(Q4)
#plt.savefig("plots/psych3.pdf")
#p = balanced(a)
#synchronize_holidays(p)
#print(p)

#b5 = balanced(a)
#b6 = balanced3(a)
#print(np.shape(b5)[0])
#synchronize_holidays(b5)
#synchronize_holidays6(b6)
#s5 = np.sum(b5, axis=0)
#s6 = np.sum(b6, axis=0)
#print(s5.mean(), s6.mean())

#p = balanced(a)
#weird_holiday_idea(p)
#s = np.sum(p, axis=0)
#print(s.mean())
#
#Q5 = computeQ(a,s)
#plt.plot(Q5)
#plt.savefig("plots/psych5.pdf")



