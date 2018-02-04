
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

# nice, this generates our range and step:
t1 = np.arange(-5.0, 5.0, 1)
t2 = np.arange(0.0, 5.0, 0.02)

def g(x):
    return x ** 3

plt.plot(t1, g(t1), 'bo')
plt.show()

# plt.figure(1)
# # same as 2, 1, 2: means 2 rows, 1 column, and this is the first:
# plt.subplot(211)
# # 'k' must mean continous line:
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()

# Lets us create multiple figures, i.e. open up multiple chart windows:
# plt.figure(1)                # the first figure
# ax1 = plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# ax2 = plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])
#
# plt.figure(2)                # a second figure
# ax3 = plt.plot([4, 5, 6])          # creates a subplot(111) by default
#
# plt.figure(1)                # figure 1 current; subplot(212) still current
# plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
#
# plt.show()
# Note: use this to set bounds for x and y axes:
# plt.axis([40, 160, 0, 0.03])

# Use this to see a grid:
# plt.grid(True)
