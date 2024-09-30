#Take 2.subhradip

#Every 4 digit natural number(n) where all 4 digits are unique (say, of the form 'abcd'),
#   when rearranged in asc(nA) and desc(nD) order of digits
#     and the difference of nA and nD is taken as the new n
#      will end up giving us 6174, the KAPREKAR constant
#      (given there have been enough repetitions of the said algorithm)

#This program tells us what the maximum number of repetitions is when we consider all 4 digit numbers
#It also tells us the number of repetitions for each such 4 digit number until it converges to 6174

countSET=set()

for n in range(1023, 9877):
    
    nSTR=str(n)
    checkSET=set()
    
    for i in range(len(nSTR)):
        for j in range(i+1, len(nSTR)):
            
            checkSET.add(nSTR[i]!=nSTR[j])
            
    if checkSET=={True}:
        
        print(f"TEST for {n}")
        
        STEPcount=0
        
        while n!=6174:
            
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


