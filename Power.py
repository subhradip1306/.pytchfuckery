import math
import random

n=int(input("What is the cardinality of the set? "))
setX=set()
setY=set()

for i in range(n):
    x=(input("Please enter an element: "))
    
    setX.add(x)
    setY.add(x)

subset=set()
subset.update(setY)

powerset={frozenset(setX), frozenset(set())}

if len(setX)>1:

    for k in range(2**(n+int(n/2))):
        subLIST=list(subset)
                
        m=random.randint(0, len(subset)-1)
                
        subLIST.pop(m)
        subset=set(subLIST)
                
        powerset.add(frozenset(subset))
                
        if len(subset)==1:
            
            subset.update(setY)
    
    
powerLIST=list(powerset)

for j in range(len(powerset)):
    print(powerLIST[j])   

print(len(powerset))
