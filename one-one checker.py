#Take1.subhradip

#Checks one-one for functions whose domain is Z

import math

y=input("Input f(x): ")

x=0
n=-1
xpts=[]
ypts=[]

checkSET={True}

oneone=True

while oneone:
    n+=1
    
    print(f'{n}th turn')
    
    x=n
    xpts.append(x)
    ypts.append(eval(y))
        
        
    x=-n
    xpts.append(x)
    ypts.append(eval(y))
       
        
    if len(ypts)==2:
        ypts.pop(0)
        xpts.pop(0)
            
    if len(ypts)>1:
        for i in range(len(ypts)):
            for j in range(i+1, len(ypts)):
                
                checkSET.add(ypts[i]!=ypts[j])
                    
                if checkSET!={True}:
                    
                    print(f"f(x) is not distinct for x={xpts[i]} and x={xpts[j]}")   
                    oneone=False
                    
                    break
                
            if checkSET!={True}:
                break
                
              
    if checkSET=={True}:
        print("f(x) is probably or potentially one-one")
        
        

print (xpts)
print (ypts)

print("f(x) is NOT one-one")