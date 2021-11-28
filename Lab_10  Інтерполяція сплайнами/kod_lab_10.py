import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *

x = [0.2, 0.6, 1.1, 1.8, 2.6]
y = [3.34, 4.53, 2.75, 3.91, 3.57]

spl = UnivariateSpline(x,y)
xs = linspace(-9, 9, 1000)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.plot(x,y, 'ro', label = 'координати перетину x та y', color = 'r')
plt.title('Інтерполяція сплайнами')
plt.plot(xs, spl(xs), 'g')
plt.legend()
plt.show()
