from matplotlib import pyplot as plt
import numpy as np
import math

def log(num):
    return math.log(num)

def exponential(num, base):
    return math.pow(base, num)

logX = np.vectorize(log)
exponentiate = np.vectorize(exponential)
xValues = np.arange(-40,41,0.01)
yValues = exponentiate(xValues, 2)
colours = ['m', 'g', 'r', 'b']

xMin, xMax, yMin, yMax = -50, 50, -50, 50
tickFrequency = 5

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(xValues, yValues)

ax.set(xlim=(xMin-1, xMax+1), ylim=(yMin-1, yMax+1), aspect='equal')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

x_ticks = np.arange(xMin, xMax+1, tickFrequency)
y_ticks = np.arange(yMin, yMax+1, tickFrequency)
ax.set_xticks(x_ticks[x_ticks != 0])
ax.set_yticks(y_ticks[y_ticks != 0])

ax.set_xticks(np.arange(xMin, xMax+1, 5), minor=True)
ax.set_yticks(np.arange(yMin, yMax+1, 5), minor=True)

ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

plt.show()

