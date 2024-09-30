#Golden Spiral made by Subhradip
#I love myself man, I'm the GOAT
import matplotlib.pyplot as plt
import numpy as np
import math

t=0

x=[((math.sin(t)*((1+math.sqrt(5))/2))*t/(3.14))]
y=[((math.cos(t)*((1+math.sqrt(5))/2))*t/(3.14))]

while t<10:
    t+=0.1

    x.append((math.sin(t)*((1+math.sqrt(5))/2))*t/(3.14))
    y.append((math.cos(t)*((1+math.sqrt(5))/2))*t/(3.14))
    
print(x)
print(y)

plt.grid(True)
plt.plot(x,y)
plt.show()