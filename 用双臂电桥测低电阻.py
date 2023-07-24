import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft YaHei", size=13)

fig, axs = plt.subplots()

t = [30.9, 35.8, 41.4, 45.9, 50.0, 55.0, 60.0, 66.1, 71.0, 77.1]
R = [4.490e-3, 4.58e-3, 4.68e-3, 4.76e-3, 4.833e-3, 4.927e-3, 5.004e-3, 5.110e-3, 5.194e-3, 5.300e-3]
Rx = [4.490, 4.58, 4.68, 4.76, 4.833, 4.927, 5.004, 5.110, 5.194, 5.300]

axs.scatter(t, Rx)
axs.set_title("Rt-t 特性曲线", weight="bold", size=20)
axs.set_xlabel("t/℃", weight="bold", size=16)
axs.set_ylabel("Rt/$10^{-3}$Ω", weight="bold", size=16)
axs.xaxis.set_major_formatter('{x:1.1f}')
axs.yaxis.set_major_formatter('{x:1.3f}')
axs.grid(True)
for t_, R_ in zip(t, Rx):
    axs.text(t_ - 2, R_, "({0:.1f}, {1:.3f})".format(t_, R_), ha="right", va="center")

linear_model = np.polyfit(t, Rx, 1)
print(f"linear model of Rt-t: Rt = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
print(linear_model_fn)
x_s = np.arange(20, 80)
axs.plot(x_s, linear_model_fn(x_s), "b--")

R0 = linear_model[1]
R0_alpha = linear_model[0]
alpha_ = R0_alpha / R0
print(
    f"alpha calculated by Rt-t graph: {alpha_}"
)

plt.show()