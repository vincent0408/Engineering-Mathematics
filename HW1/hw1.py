from math import sqrt, sin
from matplotlib import pyplot as plt
import numpy as np
import os
plt.style.use('ggplot')

step = 0.02
x_n = 0
y_n = 1

def first_order_de(x, y):
    return sin(sqrt(x) + sqrt(y))

def euler_method(x_n,  y_n):
    return y_n + step * first_order_de(x_n, y_n)

def modified_euler_method(x_n, y_n):
    predict_y_n1 = euler_method(x_n, y_n)
    return y_n + step * (first_order_de(x_n, y_n) + first_order_de(x_n + step, predict_y_n1)) / 2

def RK4(x_n, y_n):
    k1 = first_order_de(x_n, y_n)
    k2 = first_order_de(x_n + 0.5 * step, y_n + 0.5 * step * k1)
    k3 = first_order_de(x_n + 0.5 * step, y_n + 0.5 * step * k2)
    k4 = first_order_de(x_n + step, y_n + step * k3)
    return y_n + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

em, mem, rk4 = np.zeros(501), np.zeros(501), np.zeros(501)

em[0] = y_n
mem[0] = y_n
rk4[0] = y_n

for n, i in enumerate(np.arange(0, 10, step)):
    try:
        em[n + 1] = euler_method(i, em[n])
        mem[n + 1] = modified_euler_method(i, mem[n])
        rk4[n + 1] = RK4(i, rk4[n])
    except:
        break
    print('{}, {:.5f}, {:.5f}, {:.5f}'.format(n + 1, em[n + 1], mem[n + 1], rk4[n + 1]))

plt.figure(figsize=(15,6))
plt.title('Numerical Methods')
plt.scatter(np.arange(0, 10 + step, step), em, s=1, label = 'Euler\'s Method')
plt.scatter(np.arange(0, 10 + step, step), mem, s=1,  label = 'Improved Euler\'s Method')
plt.scatter(np.arange(0, 10 + step, step), rk4, s=1, label = 'RK4')
plt.xticks([x for x in np.arange(0, 10 + step, step) if x % 1 == 0])
plt.legend(markerscale=2)

os.makedirs('./HW1', exist_ok=True)
plt.savefig('./HW1/hw1.png', bbox_inches='tight', dpi=1000)
#plt.show()