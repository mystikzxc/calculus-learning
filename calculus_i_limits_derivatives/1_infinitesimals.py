import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000) # start, finish, n points

# If x² + 2x + 2:
y = x**2 + 2*x + 2

# plot and display figure
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()

'''
- There are no straight lines on curve
- If zoom infinitely close, we observe curves that approach lines
- This enables us to find slope m (tangent) anywhere on the curve, including to identify where m = 0:
'''

# fig, ax = plt.subplots()
# ax.set_xlim([-2, -0])
# ax.set_ylim([0, 2])
# ax.plot(x, y)
# plt.show()

# fig, ax = plt.subplots()
# ax.set_xlim([-1.5, -0.5])
# ax.set_ylim([0.5, 1.5])
# ax.plot(x, y)
# plt.show()

# fig, ax = plt.subplots()
# ax.set_xlim([-1.1, -0.9])
# ax.set_ylim([0.9, 1.1])
# ax.plot(x, y)
# plt.show()

fig, ax = plt.subplots()
ax.set_xlim([-1.01, -0.99])
ax.set_ylim([0.99, 1.01])
ax.plot(x, y)
plt.show()