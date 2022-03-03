from collections import defaultdict
import matplotlib.pyplot as plt

U = defaultdict(float, {x: 0.1 for x in range(-5, 6)})
S2 = defaultdict(float)
S3 = defaultdict(float)
S4 = defaultdict(float)
for i, pi in U.items():
    for j, pj in U.items():
        S2[i + j] += pi * pj

for i, pi in S2.items():
    for j, pj in U.items():
        S3[i + j] += pi * pj

for i, pi in S3.items():
    for j, pj in U.items():
        S4[i + j] += pi * pj
 
support = sorted(S4.keys())
pdf = [S2[i] for i in support]
pdf2 = [S3[i] for i in support]
pdf3 = [S4[i] for i in support]

plt.plot(support, pdf, 'o', color='blue')
plt.plot(support, pdf2, 'o', color='red')
plt.plot(support, pdf3, 'o', color='orange')

plt.vlines(support, 0, pdf, color='blue')
plt.vlines(support, 0, pdf2, color='red')
plt.vlines(support, 0, pdf3, color='orange')

plt.ylim(bottom=0)
plt.savefig("figures/S4.ps")

