import math
import random
import numpy as np 

a = np.matrix([[1,-2,3],[4,2,-3],[3,-3,5]])

n = 3
i = 0
b = np.matrix([[-5],[0],[-9]])
# Ann*Xn = Bn
print(a)
k=1
while k<= n - 1:
    
    while i <= n:
        j = k 
        b[i] = b[i] - (a[i][k]/a[k][k])*b[k]
        while j <= n:
            a[i][j] = [i][j] - (a[i][k]/a[k][k])*a[k][j]
            j += j + 1
        i += i + 1
    k += k + 1
    i = k + 1
