import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

mu0 = 4 * np.pi * 10 ** -7
N0 = 400
I = 0.4
R = 0.1

plt.rc("font", family="Microsoft YaHei", size=12)
fig, axs = plt.subplots(3, 1, figsize = (8, 8), tight_layout = True)

x1 = np.arange(-5, 5.1, 1)
B1 = np.array([0.728, 0.813, 0.893, 0.956, 0.996, 1.013, 0.997, 0.955, 0.891, 0.810, 0.729])
x0 = np.arange(-0.05, 0.05, 0.0001)
B0 = mu0 * N0 * I * R ** 2 / (2 * (R ** 2 + x0 ** 2) ** 1.5) * 1000

B1_ = make_interp_spline(x1 * 0.01, B1)

axs[0].set_title("单个载流圆线圈轴线上磁场分布", weight = "bold")
axs[0].spines[["left"]].set_position(("data", 0))
axs[0].spines[["bottom"]].set_position(("data", 0.715))
axs[0].spines[["top", "right"]].set_visible(False)
axs[0].scatter(x1, B1)
axs[0].plot(x0 * 100, B1_(x0), label = "测得磁场", linewidth = 1)
axs[0].plot(x0 * 100, B0, 'r--', label = "理想磁场", linewidth = 2)
axs[0].legend(loc = "upper left")
axs[0].axvline(color = "black", linewidth = 2)
axs[0].axhline(0.715, color = "black", linewidth = 2)
axs[0].set_xlabel(r"$X(10^{-2}m)$", weight = "bold")
axs[0].set_ylabel(r"$B(mT)$", weight = "bold")
axs[0].plot(1, 0.715, ">k", transform=axs[0].get_yaxis_transform(), clip_on=False)
axs[0].plot(0, 1, "^k", transform=axs[0].get_xaxis_transform(), clip_on=False)
axs[0].xaxis.set_ticks(x1)
axs[0].yaxis.set_major_locator(plt.MultipleLocator(0.05))

y = x1
y0 = x0
By = np.array([1.225, 1.133, 1.068, 1.027, 1.008, 1.004, 1.011, 1.036, 1.083, 1.155, 1.262])

By_ = make_interp_spline(y * 0.01, By)

axs[1].set_title("单个载流圆线圈中心平面内径向磁场分布", weight = "bold")
axs[1].spines[["left"]].set_position(("data", 0))
axs[1].spines[["bottom"]].set_position(("data", 0.98))
axs[1].spines[["top", "right"]].set_visible(False)
axs[1].scatter(y, By)
axs[1].plot(y0 * 100, By_(y0), label = "测得磁场")
axs[1].legend(loc = "upper left")
axs[1].axvline(color = "black", linewidth = 2)
axs[1].axhline(0.98, color = "black", linewidth = 2)
axs[1].set_xlabel(r"$Y(10^{-2}m)$", weight = "bold")
axs[1].set_ylabel(r"$B(mT)$", weight = "bold")
axs[1].plot(1, 0.98, ">k", transform=axs[1].get_yaxis_transform(), clip_on=False)
axs[1].plot(0, 1, "^k", transform=axs[1].get_xaxis_transform(), clip_on=False)
axs[1].xaxis.set_ticks(y)
axs[1].yaxis.set_major_locator(plt.MultipleLocator(0.05))

x2 = np.arange(-10, 10.1, 1)
B2 = np.array([0.899, 1.006, 1.112, 1.208, 1.288, 1.346, 1.386, 1.400, 1.406, 1.409, 1.408, 1.409, 1.412, 1.409, 1.391, 1.360, 1.305, 1.226, 1.132, 1.022, 0.916])

B2_ = make_interp_spline(x2 * 0.01, B2)
x2_ = np.arange(-0.1, 0.1, 0.0001)

B20 = mu0 * N0 * I * R ** 2 / (2 * (R ** 2 + (x2_ + 0.5 * R) ** 2) ** 1.5) * 1000 + \
      mu0 * N0 * I * R ** 2 / (2 * (R ** 2 + (x2_ - 0.5 * R) ** 2) ** 1.5) * 1000

axs[2].set_title("亥姆霍兹线圈轴线上磁场分布", weight = "bold")
axs[2].spines[["left"]].set_position(("data", 0))
axs[2].spines[["bottom"]].set_position(("data", 0.87))
axs[2].spines[["top", "right"]].set_visible(False)
axs[2].scatter(x2, B2)
axs[2].plot(x2_ * 100, B2_(x2_), label = "测得磁场", linewidth = 1)
axs[2].plot(x2_ * 100, B20, 'r--', label = "理想磁场", linewidth = 2)
axs[2].legend(loc = "upper left")
axs[2].axvline(color = "black", linewidth = 2)
axs[2].axhline(0.87, color = "black", linewidth = 2)
axs[2].set_xlabel(r"$X(10^{-2}m)$", weight = "bold")
axs[2].set_ylabel(r"$B(mT)$", weight = "bold")
axs[2].plot(1, 0.87, ">k", transform=axs[2].get_yaxis_transform(), clip_on=False)
axs[2].plot(0, 1, "^k", transform=axs[2].get_xaxis_transform(), clip_on=False)
axs[2].xaxis.set_ticks(x2[::2])
axs[2].yaxis.set_major_locator(plt.MultipleLocator(0.1))

for i in range(3): 
    axs[i].xaxis.set_major_formatter('{x:1.2f}')
    axs[i].yaxis.set_major_formatter('{x:1.3f}')
    axs[i].grid(True)

plt.show()