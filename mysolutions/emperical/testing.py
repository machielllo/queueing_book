from collections import defaultdict
import matplotlib.pyplot as plt

U = defaultdict(float, {x: 0.05 for x in range(-10, 10)})
S2 = defaultdict(float)
for i, pi in U.items():
    for j, pj in U.items():
        S2[i + j] += pi * pj
 
support = sorted(S2.keys())
pdf = [S2[i] for i in support]
pdf2 = [U[i] for i in support]

plt.plot(support, pdf, 'o')
#plt.plot(support, pdf2, 'o')
plt.vlines(support, 0, pdf)
#plt.vlines(support, 0, pdf2, color='orange')
plt.ylim(bottom=0)
plt.savefig("figures/S2.pdf")
