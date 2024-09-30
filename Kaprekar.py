#Take 4.subhradip

#Find numbers n such that if abc...z are the digits of n
#if we rearrange these digits in the asc. and desc. order
#and name the two arrangements nA and nD resp.
#then the difference of nA and nD will be equal to n

# EG: 495
#     954-459=495
#     des asc  n

BOOLcount=0
n=99
k=int(input("How many such numbers do you want? "))
while BOOLcount<k:
    n+=1
    nSTR=str(n)
    listX=list()
    
    for i in range(len(nSTR)):
        listX.append(nSTR[i])
        
    xLOW=sorted(listX)
    xHIGH=reversed(xLOW)
    
    lowSTR="".join(xLOW)    
    highSTR="".join(xHIGH)
    
    nLOW=int(lowSTR)
    nHIGH=int(highSTR)
    
    nDIFF=nHIGH-nLOW
    
    if nDIFF==n:
        BOOLcount+=1
        print(n)
        
print(f"BOOLcount is {BOOLcount}") 