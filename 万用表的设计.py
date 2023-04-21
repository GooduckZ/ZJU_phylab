import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

x1 = [1.00, 2.00, 3.00, 4.00, 5.00]
x2 = [0.50, 1.00, 1.50, 2.00, 2.50, 3.00, 3.50, 4.00, 4.50]

plt.rc("font", family="Microsoft YaHei", size=13)
fig, axs = plt.subplot_mosaic([["ul", "r"],["ll", "r"]], figsize=(12, 8), layout='constrained')

axs['ul'].set_title(r"改装电流表校准曲线", weight="bold", size=20)
I1 = [0.97, 1.96, 2.93, 3.89, 4.92]
dI = [0.03, 0.04, 0.07, 0.11, 0.08]

l1, = axs['ul'].plot(x1, I1, "ro--")
axs['ul'].set_xlabel(r"$I$改$/mA$", size=16)
axs['ul'].set_ylabel(r"$I$准$/mA$", size=16)
axs['ul'].xaxis.set_major_formatter('{x:1.2f}')
axs['ul'].yaxis.set_major_formatter('{x:1.2f}')
axs['ul'].grid(True)
ax1 = axs['ul'].twinx()
l2, = ax1.plot(x1, dI, "bo-")
ax1.set_ylabel(r"$\Delta I/mA$", size=16)
ax1.yaxis.set_major_formatter('{x:1.2f}')
ax1.legend([l1, l2], [r"I准", r"$\Delta I$"], loc="upper left")

axs['ll'].set_title(r"改装电压表校准曲线", weight="bold", size=20)
U1 = [1.01, 2.04, 3.00, 3.95, 4.96]
dU = [-0.01, -0.04, 0.00, 0.05, 0.04]

l1, = axs['ll'].plot(x1, U1, "ro--")
axs['ll'].set_xlabel(r"$U$改$/V$", size=16)
axs['ll'].set_ylabel(r"$U$准$/V$", size=16)
axs['ll'].xaxis.set_major_formatter('{x:1.2f}')
axs['ll'].yaxis.set_major_formatter('{x:1.2f}')
axs['ll'].grid(True)
ax2 = axs['ll'].twinx()
l2, = ax2.plot(x1, dU, "bo-")
ax2.set_ylabel(r"$\Delta U/V$", weight="bold", size=16)
ax2.yaxis.set_major_formatter('{x:1.2f}')
ax2.legend([l1, l2], [r"U准", r"$\Delta U$"], loc="upper left")

def forward(x):
    return np.log(x)

def inverse(x):
    return np.exp(x)

axs['r'].set_title(r"$R_x-I_x$曲线", weight="bold", size=20)
Rx = [2490.0, 1160.0, 680.0, 440.0, 296.0, 200.0, 131.0, 79.7, 36.3]
x0 = np.arange(0.4, 4.7, 0.01)
Rx_ = make_interp_spline(x2, Rx)(x0)
ticks = [20, 50, 100, 200, 500, 1000, 2000]
axs['r'].set_yscale('log')
axs['r'].plot(x0, Rx_, "k-", lw=2)
axs['r'].scatter(x2, Rx, c='r', marker='o', s=50)
axs['r'].set_xlabel(r"$I_x/mA$", size=16)
axs['r'].set_ylabel(r"$R_x/\Omega$", size=16)
axs['r'].xaxis.set_major_formatter('{x:1.2f}')
axs['r'].yaxis.set_major_formatter('{x:1.1f}')
axs['r'].set_yticks(ticks)
axs['r'].grid(True)
for I_, R_ in zip(x2, Rx):
    axs['r'].annotate("(%.2f,%.1f)" % (I_, R_), xy=(I_, R_), xytext=(I_+0.1, R_+0.1), size=12)
axs['r'].set_xlim(0.2, 5.6)
plt.show()

