import matplotlib.pyplot as plt
import numpy as np
import math
x= [3.5,3.6,3.7,3.8,3.9,4.0]
y= [33.1154,36.5982,40.4473,44.7012,49.4024,54.5982]
h = x[1] - x[0]

def dy(y,j):
  m1 = []
  for i in range(len(y)):
     m1.append(y[i] - y[i-1])
  m1.pop(0)
  if j == 1:
    return m1
  else:
    j-=1
    return dy(m1,j)
#return m1
#print(dy(y,j))
xprom1 = 3.522
xprom2 = 3.905

#Перша інтерполяційна формула Ньютона
q1 = (xprom1-x[0])/h

Nx1 = y[0] + q1*dy(y,1)[0] + ((q1*(q1-1))/math.factorial(2)) * dy(y,2)[0] + ((q1*(q1-1)*(q1-2))/math.factorial(3))*dy(y,3)[0] + ((q1*(q1-1)*(q1-2)*(q1-3))/math.factorial(4)) * dy(y,4)[0] + ((q1*(q1-1)*(q1-2)*(q1-3)*(q1-4))/math.factorial(5)) * dy(y,5)[0]
print('Перша інтерполяційна формула Ньютона f(3,522) = ', Nx1)

#Друга інтерполяційна формула Ньютона
q2 = (xprom2 - x[5])/h

Nx2 = y[5] + q2*dy(y,1)[4] + ((q2*(q2+1))/math.factorial(2) )*dy(y,2)[3] + ((q2*(q2+1)*(q2+2))/math.factorial(3))*dy(y,3)[2] + ((q2*(q2+1)*(q2+2)*(q2+3))/math.factorial(4))*dy(y,4)[1] + ((q2*(q2+1)*(q2+2)*(q2+3)*(q2+4))/math.factorial(5))*dy(y,5)[0]

print('Друга інтерполяційна формула Ньютона f(3,905) = ', Nx2)

newX = [3.522, 3.905]
newY = [Nx1,Nx2]

plt.grid(True) # setka 
plt.plot(x, y, 'g--' # маркер 
)  
plt.plot(newX, newY, 'ro')
plt.plot(x, y, 'go')
# з'єднані суцільною лінією 
plt.xlabel('x') #pid osey 
plt.ylabel('y') 
plt.title('Графік Перетину функцій') 
plt.legend(['X and y','Nx1, Nx2',' x/y ' ], loc='upper left')


# положення легенди 
plt.show()
