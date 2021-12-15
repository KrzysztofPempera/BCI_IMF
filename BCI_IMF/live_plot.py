import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

fig = plt.figure()
ax1 = fig.add_subplot(8,1,1)
ax2 = fig.add_subplot(8,1,2)
ax3 = fig.add_subplot(8,1,3)
ax4 = fig.add_subplot(8,1,4)
ax5 = fig.add_subplot(8,1,5)
ax6 = fig.add_subplot(8,1,6)
ax7 = fig.add_subplot(8,1,7)
ax8 = fig.add_subplot(8,1,8)

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))

    ax1.cla()
    ax1.plot(x_vals,y_vals)

    ax2.cla()
    ax2.plot(x_vals,y_vals)

    ax3.cla()
    ax3.plot(x_vals,y_vals)

    ax4.cla()
    ax4.plot(x_vals,y_vals)

    ax5.cla()
    ax5.plot(x_vals,y_vals)

    ax6.cla()
    ax6.plot(x_vals,y_vals)

    ax7.cla()
    ax7.plot(x_vals,y_vals)

    ax8.cla()
    ax8.plot(x_vals,y_vals)

ani = FuncAnimation(fig, animate, interval = 1000)

fig.set_figwidth(14)
fig.set_figheight(8)

plt.tight_layout()
plt.show()

class LivePlot():