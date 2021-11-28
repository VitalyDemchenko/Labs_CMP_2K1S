import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import math as m
x = linspace(-10, 10,100)
y = 1 + x + x**2/2
xn = linspace(-10, 10,100)
t = e**sin(xn)
#y = e**sin(x)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.yticks(range(-50,65,5))

xx = range(1)
yy = range(60)
[plt.plot([x,x],[min(yy),max(yy)],color='k') for x in xx]
[plt.plot([min(xx),max(xx)],[y,y],color='k') for y in yy]

xx = range(9)
yy = range(1)
[plt.plot([x,x],[min(yy),max(yy)],color='k') for x in xx]
[plt.plot([min(xx),max(xx)],[y,y],color='k') for y in yy]


plt.plot(x, y, 'r--', label = ' y = 1 + x + x^2/2 ', color = 'r')
plt.plot(xn, t, 'g--', label = ' y = e^sin(x)', color = 'g')
plt.title(' Графік f(x) = e^sin(x) та наближення ')

plt.legend()
plt.show()
