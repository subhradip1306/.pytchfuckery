#Take 3.subhradip

#Are 631764, 63317664, etc. similar to kaprekar constant for 6 and 8 digit numbers?
#*549945
countSET=set()

for n in range(102345, 987655):
    
    nSTR=str(n)
    checkSET=set()
    
    for i in range(len(nSTR)):
        for j in range(i+1, len(nSTR)):
            
            checkSET.add(nSTR[i]!=nSTR[j])
            
    if checkSET=={True}:
        
        print(f"TEST for {n}")
        
        STEPcount=0
        
        while n!=631764:
            
            nSTR=str(n)
            
            lowX=sorted(nSTR)
            highX=reversed(lowX)
            
            lowSTR="".join(lowX)
            highSTR="".join(highX)
            
            nLOW=int(lowSTR)
            nHIGH=int(highSTR)
            
            n=nHIGH-nLOW
            
            STEPcount+=1
            print(f"  {n}")
        print(f"   STEPcount is {STEPcount}")
        countSET.add(STEPcount)

countLIST=list(countSET)
countLIST=sorted(countLIST)

HESTcount=countLIST[len(countLIST)-1]
print(f"{HESTcount} is the highest STEPcount recorded")



