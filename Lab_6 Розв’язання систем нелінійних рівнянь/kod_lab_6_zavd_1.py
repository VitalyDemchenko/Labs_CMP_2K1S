from scipy import optimize
import math

def fun(x):
    return[math.sin(x[0] + 0.5) - x[1] - 1, math.cos(x[1] - 2) + x[0]]
sol = optimize.root(fun,[0,0], method = 'hybr')

print(sol.x)
