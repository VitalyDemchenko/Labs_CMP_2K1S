import numpy as np
from numpy import *
import math
from scipy import integrate
from numpy import *
import math as m
import matplotlib.pyplot as plt

x1 = []
y1 = []
h1 = 0.1
x10 = 1.7
y10 = 5.3
i1 = 0
x1i = x10
y1i = y10
x1ip1 = 0
y1ip1 = 0
y1.append(y1i)
x1.append(x1i)
while i1 < 10:
    x1ip1 = x1i + h1
    y1ip1 = y1i + 0.1*(x1i + cos(y1i/3.14159))
    x1ip1 = float('{:.3f}'.format(x1ip1))
    y1ip1 = float('{:.5f}'.format(y1ip1))
    y1.append(y1ip1)
    x1.append(x1ip1)
    x1i = x1ip1
    y1i = y1ip1
    i1 += 1


print('x= ', x1)
print('y= ', y1)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Метод Ейлера')
plt.plot(x1,y1, 'g--', label = 'eiler')
plt.plot(x1,y1, 'ro', label = 'x and y')

plt.legend()
plt.show()


