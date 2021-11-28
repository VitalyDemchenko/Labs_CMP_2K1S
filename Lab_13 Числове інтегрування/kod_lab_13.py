import numpy as np
from numpy import *
import math
from scipy import integrate
from numpy import *
import math as m

# Zavd 1
def f1(x):
  return 1/sqrt(2*x + 3)
x1 = [0.8,0.86,0.92,0.98,1.04,1.1,1.16,1.22,1.28,1.34,1.4]
y1 = []
iv1 = 0
i1 = 0
i1LS = 0
i1RS = 1
h1 = 0.06
sumYR = 0
sumYL = 0

while i1 < len(x1):
    y1.append(f1(x1[i1]))
    i1 += 1
#print(y1)

#left
while i1LS < (len(y1) - 1):
  sumYL += y1[i1LS]
  i1LS += 1
Left = h1*sumYL
print(' Ліві прямокутники ', Left)

#right    
while i1RS < (len(y1)):
  sumYR += y1[i1RS]
  i1RS += 1
Right = h1*sumYR
print(' Праві прямокутники ', Right)

#middle
x1m = [0.83,0.89,0.95,1.01,1.07,1.13,1.19,1.25,1.31,1.37]
y1m = []
i1m = 0
sumYM = 0
i1M = 0
Middle = 0
i1MS = 0
while i1m < len(x1m):
    y1m.append(f1(x1m[i1m]))
    i1m += 1
#print(y1m)
while i1MS < len(y1m):
    sumYM += y1m[i1MS]
    i1MS += 1
Middle = h1*sumYM
print(' Середні прямокутники ', Middle)
v,err = integrate.quad(f1,0.8,1.4)
print (' Перевірка',v)
print('   ')

# Zavd 2
def f2(x):
  return sqrt(x)*cos(x**2)
h2 = 0.1
x2 = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2]
y2 = []
i2 = 0
Simpson = 0
while i2 < len(x2):
    y2.append(f2(x2[i2]))
    i2 += 1
#print(y2)

Simpson = (h2/3)*(y2[0] + y2[8]+ 4*(y2[1] + y2[3] + y2[5] + y2[7]) + 2*(y2[2] + y2[4] + y2[6]))
print(' Метод сімпсона ', Simpson)

v,err = integrate.quad(f2,0.4,1.2)
print (' Перевірка ',v)
print('   ')
# Zavd 3

def f3(x):
  return 1/sqrt(3*x**2 - 0.4)

x3 = [1.3, 1.34, 1.38, 1.42, 1.46, 1.5, 1.54, 1.58, 1.62, 1.66, 1.7, 1.74, 1.78, 1.82, 1.86, 1.9, 1.94,1.98,2.02, 2.06, 2.1]
y3 = []
i3 = 0
h3 = 0.04
sumY3 = 0
i3s = 1
while i3 < len(x3):
    y3.append(f3(x3[i3]))
    i3 += 1
#print(y3)

while i3s < len(y3) - 1:
    sumY3 += y3[i3s]
    i3s += 1
#print('sum', sumY3)

Trapec = h3*((y3[0] + y3[20])/2 + sumY3)
print(' Метод трапецій ', Trapec)

v,err = integrate.quad(f3,1.3,2.1)
print (' Перевірка',v)
