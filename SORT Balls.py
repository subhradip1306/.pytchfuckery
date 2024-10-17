#Smallest number of swaps reqd to sort balls

import random

random.seed()
leng=int(1+10*(random.random()))

print(leng)

INITIAL=[]

for i in range(leng):
    
    dig=random.randint(0,1)
    dig=str(dig)
    INITIAL.append(dig)

INITIALstr=''.join(INITIAL)
print(INITIALstr)

checkA=[]
checkB=[]

for j in range(int(leng/2)):
    
    if INITIAL[j]!=INITIAL[0]:
        checkA.append(j)
 
for k in range(leng-int(leng/2)):
    if INITIAL[leng-k]==INITIAL[0]:
        checkB.append(leng-k)
        
print(checkA) 
print(checkB)
  
n=0

for l in checkA:
    try:
        INITIALstr[l], INITIALstr[checkB[n]]=INITIALstr[checkB[n]], INITIALstr[l]

    n+=1

    except: 
        break