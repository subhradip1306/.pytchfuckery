import math

n=int(input("What is the cardinality of the set? "))
setX=set()
setY=set()

for i in range(n):
    x=int(input("Please enter an element: "))
    
    setX.add(x)
    setY.add(x)
subset=set()
subset.update(setY)
print(setX)
print(subset)
powerset={frozenset(setX), frozenset(set())}
for k in range(2**n):
    
    for m in setX:
            subset.remove(m)
            print("subset is", subset)
            powerset.add(frozenset(subset))
            
            if len(subset)==1:
                print(setY)
                subset.update(setY)
                print("jhingalala", subset)
print(powerset)   
print(len(powerset))