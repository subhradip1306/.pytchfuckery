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


if len(checkA)>=len(checkB):
    for l in len(checkA):
        try:
            INITIALstr[checkA[l]], INITIALstr[checkB[l]=INITIALstr[checkB[l]], INITIALstr[checkA[l]]

        except: 
            break

else:
    for l in len(checkB):
        try:
            INITIALstr[checkA[l]], INITIALstr[checkB[l]=INITIALstr[checkB[l]], INITIALstr[checkA[l]]

        except: 
            break