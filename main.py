import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 20, 0.1)
b = 4


def Sinfunc(x, a, b):
    return np.sin((x / b) + a)


fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 3)

line1, = ax1.plot(x, Sinfunc(x, 1, 1), linestyle="--", label="Traveling Wave_1")
line2, = ax1.plot(x, Sinfunc(x, -1, 2), linestyle="--", label="Traveling Wave_2")
line3, = ax1.plot(x, Sinfunc(x, 1, 1) + Sinfunc(x, -1, 2), label="Standing Wave")
line4, = ax2.plot(x, Sinfunc(x, 1, 1) + Sinfunc(x, -1, 2), label="Standing Wave")

ax1.set_title("Traveling waves with Standing wave")

ax2.set_title("Standing wave only")
ax1.set_ylim(3, -3)
ax2.set_ylim(3, -3)
plt.ion()

for a in np.arange(1, 50, 0.1):
    # plt.axhline(y=0, color="black")
    line1.set_ydata(Sinfunc(x, a, 1))
    line2.set_ydata(Sinfunc(x, -a, b))
    line3.set_ydata(Sinfunc(x, a, 1) + Sinfunc(x, -a, b))
    line4.set_ydata(Sinfunc(x, a, 1) + Sinfunc(x, -a, 1))

    fig.canvas.draw()
    plt.legend(loc=1)
    plt.show()
    plt.pause(0.01)
