from numpy import * # для використання функцій exp та linspace 
import matplotlib.pyplot as plt 
def f(t): 
 return t**2 * exp(-t**2) 
t = linspace(0, 3, 51) # 51 точка між 0 та 3 
y = f(t) 
plt.plot(t, y) 
plt.show()
