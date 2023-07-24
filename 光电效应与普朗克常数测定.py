import matplotlib.pyplot as plt
import numpy as np

lamb = [365, 405, 436, 546, 577]
freq = list(map(lambda x: 3e3 / x, lamb))
U = [1.86, 1.504, 1.292, 0.74, 0.624]

plt.rc("font", family="Microsoft YaHei", size=13)
fig, ax = plt.subplots(figsize=(8, 5), layout='constrained')
ax.set_title(r"光电效应与普朗克常数测定", weight="bold", size=20)
ax.scatter(freq, U, c='r', marker='o', s=50)
ax.set_xlabel(r"$\nu/10^{14}Hz$", size=16)
ax.set_ylabel(r"$U/V$", size=16)
ax.xaxis.set_major_formatter('{x:1.3f}')
ax.yaxis.set_major_formatter('{x:1.3f}')
ax.grid(True)
linear_model = np.polyfit(freq, U, 1)
print(f"linear model of U-f: U = {linear_model[0]} * f + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
print(linear_model_fn)
f_s = np.arange(5, 10)
ax.plot(f_s, linear_model_fn(f_s), "b--")
for f_, U_ in zip(freq, U):
    ax.annotate("(%.3f, %.3f)" % (f_, U_), xy=(f_, U_), xytext=(f_+0.12, U_), size=12)
h = linear_model[0] * 1.602e-19 * 1e-14
print(f"h = {h}")
h0 = 6.626e-34
Er = np.abs(h - h0) / h0
print(f"Er = {Er}")
sy = np.sqrt(np.sum((U - linear_model_fn(freq))**2) / len(U))
print(f"sy = {sy}")
UA = sy / np.sqrt(np.sum((freq - np.mean(freq))**2))
print(f"UA = {UA * 1.602e-19 * 1e-14}")
UB = h * 0.03
print(f"UB = {UB}")
UC = np.sqrt((UA * 1.602e-19 * 1e-14) ** 2 + UB ** 2)
print(f"UC = {UC}")
plt.show()