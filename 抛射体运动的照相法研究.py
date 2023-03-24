import matplotlib.pyplot as plt
import numpy as np

def fit(ax, tit, x, y, deg):
    lin_mod = np.polyfit(x, y, deg)
    fx = np.poly1d(lin_mod)
    print(tit, ":")
    for i in range(deg):
        print(lin_mod[i], "* t ^", deg - i, end = ' + ')
    print(f'{lin_mod[-1]}\n')
    dots = np.linspace(-1, n, 1000)
    ax.plot(dots, fx(dots), "g--")

def draw(ax, x, y, tit, xl, yl, deg):
    ax.set_title(tit, weight="bold", size=20)
    ax.set_xlabel(xl, weight="bold", size=16)
    ax.set_ylabel(yl, weight="bold", size=16)
    ax.scatter(x, y)
    ax.grid = True
    fit(ax, tit, x, y, deg)

T = 1/24
n = 13 # 共有 n 组数据
# x = np.array([1.8, 8.3, 15.1, 21.8, 28.5, 35.1, 41.9, 48.8, 55.4, 62.0, 68.9, 75.6, 82.5])
x = np.array([1.8, 8.2, 15.2, 21.8, 28.4, 35.2, 41.8, 48.6, 55.4, 62.1, 68.8, 75.5, 82.3])
y1 = np.array([0.9, 6.2, 10.0, 11.9, 12.1, 10.7, 7.7, 3.0, -3.4, -11.2, -21.0, -32.4, -45.4])
y = np.array([1.0, 6.2, 10.0, 11.9, 12.1, 10.7, 7.7, 3.0, -3.3, -11.3, -21.0, -32.4, -45.3])
# Ts = np.arange(0, n * T, T)
Ts = np.arange(0, n, 1)
dTs = np.arange(0.5, n - 0.5, 1)
ddTs = np.arange(1, n - 1, 1)

plt.rc("font", family="Microsoft YaHei", size=13, weight="bold")

fig, axs = plt.subplots(3, 2, figsize = (10, 8), tight_layout = False)
fig.set_figheight(8)
fig.set_figwidth(12)

draw(axs[0][0], Ts, x, r"$x-t$ 图", r"$t/T$", r"$x/cm$", 1)
draw(axs[0][1], Ts, y, r"$y-t$ 图", r"$t/T$", r"$y/cm$", 2)
draw(axs[1][0], dTs, np.diff(x), r"$v_x-t$ 图", r"$t/T$", r"$v_x/(cm/T)$", 0)
draw(axs[1][1], dTs, np.diff(y), r"$v_y-t$ 图", r"$t/T$", r"$v_y/(cm/T)$", 1)
draw(axs[2][0], ddTs, np.diff(y, 2), r"$a_y-t$ 图", r"$t/T$", r"$a_y/(cm/T^2)$", 0)
draw(axs[2][1], ddTs, np.diff(y1, 2), r"$another\ a_y-t$ 图", r"$t/T$", r"$a_y/(cm/T^2)$", 0)

axs[1][0].set_ylim(3, 9)
axs[2][0].set_ylim(-3, 0)
axs[2][1].set_ylim(-3, 0)


print(f"x = {x}\nvx = {np.diff(x)}\n y = {y}\nvy = {np.diff(y)}\nay = {np.diff(y, 2)}")

ay = np.diff(y, 2)
abar = np.average(ay)

ea = np.sqrt(np.var(ay) / 10)
eb = 0.1 / 3 ** 0.5
print(f"Error_A = {ea}\nError_B = {eb}\nError = {(ea * ea + eb * eb) ** 0.5 * 24 * 24}")

plt.show()