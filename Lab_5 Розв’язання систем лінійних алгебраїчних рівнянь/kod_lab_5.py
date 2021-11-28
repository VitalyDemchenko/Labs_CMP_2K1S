import math
import numpy as np 
a = np.matrix([[1,-2,3],[4,2,-3],[3,-3,5]])
b = np.matrix([[-5],[0],[-9]])
print ('check')
print(np.linalg.solve(a, b))
print('  ')
print('metod of jord-gauss' )
print(np.linalg.inv(a) *b)

def gauss(a,b):
    n = len(b)
    
    for k in range(1,n):
        for i in range(k + 1, n):
            if a[i,k] != 0.0:
                a[i,k:n] = a[i,k:n] - a[i,k]/a[k,k] * a[k,k:n]
                b[i] = b[i] - a[i,k]/a[k,k] + b[k]
                
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k:n], b[k:n])  )/ a[k,k]
            
    return b
    
print (gauss(np.matrix([[1,-2,3],[4,2,-3],[3,-3,5]]), np.matrix([[-5],[0],[-9]])))


