from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

size = 5
U = defaultdict(float, {x: 1/size for x in np.linspace(-2, 2 , size)})
S2 = defaultdict(float)

for i, pi in U.items():
    for j, pj in U.items():
        S2[i + j] += pi * pj
        
support = sorted(S2.keys())
pdf = [S2[i] for i in support]

plt.clf()
#plt.plot(support, pdf)
plt.plot(support, pdf, 'p')
plt.vlines(support, 0, pdf)
plt.ylim(bottom=0)
plt.savefig("figures/S2+.pdf")
