#  Y(x)= 15*sin(10*x)*cos(3*x), x=[-3...3]  
 
from numpy import * 
import matplotlib.pyplot as plt 
t = linspace(-3, 3, 51) 
y = 15*sin(10*t)*cos(3*t) 
plt.grid(True) # setka 
plt.plot(t, y, 'g--' # маркер 
)  
#t = [-5,-4,-3,-2,-1,0,1,2,3,4,5] 
plt.xticks(range(-4,5)) 
plt.yticks(range(-20,25,5))   
# з'єднані суцільною лінією 
plt.xlabel('t') 
plt.ylabel('y') 
plt.title('Plotting with markers') 
plt.legend(['15*sin(10*t)*cos(3*t)', 
  
 ], 
        
           # список легенди 
 loc='upper left') # положення легенди 
plt.show()
