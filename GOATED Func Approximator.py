#Made the Subhradip, Trishit and most importantly Deepto the GOAT
#Function Approximator
import matplotlib.pyplot as plt
import numpy as np
import math

lower=float(input("Input lower limit of domain: "))
upper=float(input("Input upper limit of domain: "))
freq=float(input("Input frequency: "))
y=input("Input y(x): ")

x=lower
xpts=[]
ypts=[]

while x<upper:
    x+=freq
    xpts.append(x)
    ypts.append(eval(y))
    
print (xpts)
print (ypts)

plt.plot(xpts, ypts)
plt.show()