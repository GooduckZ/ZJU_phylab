import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Microsoft YaHei", size=13)

# t = [20.5, 25.3, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0]
t = [17.9, 24.0, 29.0, 34.0, 39.0, 44.0, 49.0, 54.0, 59.0, 64.0]
# U = [29.3, 35.4, 41.0, 47.4, 53.3, 59.3, 65.2, 70.7]
U = [30.0, 38.9, 45.0, 50.9, 56.9, 62.8, 68.4, 73.7, 79.2, 84.3]
alphas = []
E = 1.3
alpha_expect = 0.004280

for t_, U_ in zip(t, U):
    U_ = U_ / 1000
    # alphas.append(4 * U_ / (t_ * (E - 2 * U_)))
    alphas.append(4 * U_ / ((t_+7.54)  * (E - 2 * U_)))
alpha = sum(alphas) / len(alphas)

print(f"alpha values: {alphas}")
print(f"average alpha: {alpha} with relative error {abs(alpha - alpha_expect) / alpha_expect * 100}%")

fig, axs = plt.subplots(1, 2, figsize = (13, 6), tight_layout = False)
axs[0].scatter(t, U)
axs[0].set_title("Cu50 电阻 U-t 特性曲线", weight="bold", size=20)
axs[0].set_xlabel("t/℃", weight="bold", size=16)
axs[0].set_ylabel("U/mV", weight="bold", size=16)
axs[0].xaxis.set_major_formatter('{x:1.1f}')
axs[0].yaxis.set_major_formatter('{x:1.1f}')
axs[0].grid(True)
for t_, U_ in zip(t, U):
    axs[0].text(t_ - 2, U_ + 2, "({0:.1f}, {1:.1f})".format(t_, U_), ha="right", va="center")

linear_model = np.polyfit(t, U, 1)
print(f"linear fit model of U-t: U = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
x_s = np.arange(0, 70)
axs[0].plot(x_s, linear_model_fn(x_s), "b--")

k = sum(x*y for x, y in zip(t, U)) / sum(x**2 for x in t)
print(f"proportional fit model of U-t: U = {k} * t")
print(
    f"alpha calculated by proportional fit: {4 * k / 1000 / 1.3}"
    f" with relative error {abs(4 * k / 1000 / 1.3 - alpha_expect) / alpha_expect * 100}%"
)
fn = np.poly1d([k, 0])
axs[0].plot(x_s, fn(x_s), color="red")

# t = [60.0, 55.3, 50.0, 45.0, 40.0, 35.1, 30.0, 25.2]
t = [17.9, 24.0, 29.0, 34.0, 39.0, 44.0, 49.0, 54.0, 59.0, 64.0]
# R = [63.77, 62.75, 61.60, 60.51, 59.41, 58.36, 57.19, 56.17]
R = [55.37, 56.84, 57.92, 58.99, 60.10, 61.24, 62.23, 63.30, 64.30, 65.40]

axs[1].scatter(t, R)
axs[1].set_title("Cu50 电阻 Rt-t 特性曲线", weight="bold", size=20)
axs[1].set_xlabel("t/℃", weight="bold", size=16)
axs[1].set_ylabel("Rt/Ω", weight="bold", size=16)
axs[1].xaxis.set_major_formatter('{x:1.1f}')
axs[1].yaxis.set_major_formatter('{x:1.2f}')
axs[1].grid(True)
for t_, R_ in zip(t, R):
    axs[1].text(t_ - 2, R_, "({0:.1f}, {1:.2f})".format(t_, R_), ha="right", va="center")

linear_model = np.polyfit(t, R, 1)
print(f"linear model of Rt-t: Rt = {linear_model[0]} * t + {linear_model[1]}")
linear_model_fn = np.poly1d(linear_model)
print(linear_model_fn)
x_s = np.arange(0, 70)
axs[1].plot(x_s, linear_model_fn(x_s), "b--")
axs[1].plot([0, 70], [50, 64.98], "r-")

R0 = linear_model[1]
R0_alpha = linear_model[0]
alpha_ = R0_alpha / R0
print(
    f"alpha calculated by Rt-t graph: {alpha_}"
    f" with relative error {abs(alpha_ - alpha_expect) / alpha_expect * 100}%"
)

plt.show()