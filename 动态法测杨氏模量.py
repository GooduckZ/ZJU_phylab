import numpy as np
import matplotlib.pyplot as plt

L = [0.51, 1.02, 1.53, 2.04, 2.55, 4.59, 5.10]
# f = [749.3, 748.6, 746.6, 746.0, 745.0, 744.5, 744.8]
f = [749.5, 748.5, 747, 746.3, 745.3, 744.5, 744.8]
 
L = np.array(L)
f = np.array(f)

lin_mod = np.polyfit(L, f, 2)
fx = np.poly1d(lin_mod)
R2 = 1 - np.sum((f - fx(L)) ** 2) / np.sum((f - np.mean(f)) ** 2)

dots = np.linspace(0.5, 5.5, 1000)

for i in range(2):
    print(lin_mod[i], "* t ^", 2 - i, end = ' + ')
print(f'{lin_mod[-1]}\n')
print('R2 =', R2)

a = lin_mod[0]
b = lin_mod[1]
c = lin_mod[2]

print('f0 =', fx(-b / (2 * a)), 'Hz')

plt.rc("font", family="Microsoft YaHei", size=13)
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')

ax.set_title(r"动态法测杨氏模量", weight="bold", size=20)
ax.plot(L, f, 'o')
ax.set_xlabel('L/mm')
ax.xaxis.set_major_formatter('{x:1.2f}')
ax.set_ylabel('f/Hz')
ax.plot(dots, fx(dots), "g--")
for L_, f_ in zip(L[:-2], f[:-2]):
    ax.annotate("(%.2f, %.1f)" % (L_, f_), xy=(L_, f_), xytext=(L_+0.14, f_), size=12)
for L_, f_ in zip(L[-2:], f[-2:]):
    ax.annotate("(%.2f, %.1f)" % (L_, f_), xy=(L_, f_), xytext=(L_-0.5, f_+0.3), size=12)
ax.grid(True)
plt.show()
