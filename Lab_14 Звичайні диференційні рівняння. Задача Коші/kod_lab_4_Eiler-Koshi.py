import numpy as np
from numpy import *
import math
from scipy import integrate
from numpy import *
import math as m
import matplotlib.pyplot as plt

x2 = []
y2 = []
h2 = 0.1
x20 = 0.5
y20 = 0.6
i2 = 0
x2i = x20
y2i = y20
x2ip2 = 0
y2ip2 = 0
y2.append(y2i)
x2.append(x2i)
while i2 < 10:
    x2ip2 = x2i + h2
    y2ip2 = x2i + cos(y2i/7**0.5)
    x2ip2 = float('{:.3f}'.format(x2ip2))
    y2ip2 = float('{:.5f}'.format(y2ip2))
    y2.append(y2ip2)
    x2.append(x2ip2)
    x2i = x2ip2
    y2i = y2ip2
    i2 += 1

print('x= ', x2)
print('y= ', y2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Метод Ейлера-Коші')
plt.plot(x2,y2, 'g--', label = 'eiler-koshi')
plt.plot(x2,y2, 'ro', label = 'x and y')
plt.legend()
plt.show()


