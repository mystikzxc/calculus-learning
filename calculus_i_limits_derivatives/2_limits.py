import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000) # start, end, n points

# y = x**2 + 2*x + 2

# fig, ax = plt.subplots()
# plt.axvline(x=0, color='lightgray')
# plt.axhline(y=0, color='lightgray')
# plt.xlim(-5, 10)
# plt.ylim(-10, 80)
# plt.axvline(x=5, color='purple', linestyle='--')
# plt.axhline(y=37, color='purple', linestyle='--')
# ax.plot(x, y)
# plt.show()

# lim x→1 (x²-1/x-1)
def my_fxn(my_x):
    my_y = (my_x**2 - 1) / (my_x - 1)
    return my_y

# print(my_fxn(2))

# this will give a 'division by zero' error
# print(my_fxn(1))

# infinitesimals
# closer to 1 on left
# print(my_fxn(0.9))
# print(my_fxn(0.999))

# closer to 1 on right
# print(my_fxn(1.1))
# print(my_fxn(1.001))

# y = my_fxn(x)

# fig, ax = plt.subplots()
# plt.axvline(x=0, color='lightgray')
# plt.axhline(y=0, color='lightgray')
# plt.xlim(-1, 5)
# plt.ylim(-1, 5)
# plt.axvline(x=1, color='purple', linestyle='--')
# plt.axhline(y=2, color='purple', linestyle='--')
# ax.plot(x, y)
# plt.show()

# lim x→0 sinx/x
def sin_fxn(my_x):
    my_y = np.sin(my_x)/my_x
    return my_y

# the following line results in 'division by zero' error:
# y = sin_fxn(0)

# print(sin_fxn(0.1))
# print(sin_fxn(0.001))

# print(sin_fxn(-0.1))
# print(sin_fxn(-0.001))

# y = sin_fxn(x)

# fig, ax = plt.subplots()
# plt.axvline(x=0, color='lightgray')
# plt.axhline(y=0, color='lightgray')
# plt.xlim(-10, 10)
# plt.ylim(-1, 2)
# plt.axvline(x=0, color='purple', linestyle='--')
# plt.axhline(y=1, color='purple', linestyle='--')
# ax.plot(x, y)
# plt.show()

# lim x→∞ 25/x
def inf_fxn(my_x):
    my_y = 25/my_x
    return my_y

# print(inf_fxn(1e3))
# print(inf_fxn(1e6))

y = inf_fxn(x)

# split is to left half and right half
left_x = x[x<0]
right_x = x[x>0]

left_y = inf_fxn(left_x)
right_y = inf_fxn(right_x)

fig, ax = plt.subplots()
plt.axvline(x=0, color='lightgray')
plt.axhline(y=0, color='lightgray')
plt.xlim(-10, 10)
plt.ylim(-300, 300)
ax.plot(left_x, left_y, c='C0')
ax.plot(right_x, right_y, c='C0')
plt.show()