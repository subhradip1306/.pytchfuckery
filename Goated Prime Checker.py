#8

n=int(input("Please input a number: "))
print("1 is not a prime")
if n<=1: 
    print("I'll kill myself")
    
else:
    for k in range (2, n+1):
        x=int(k/2)
        p=True

        for i in range(2, x+1):
             if k%i==0:
                p=False
        
        if p:
            print(k, "is a prime")
        else:
            print(k, "is not a prime")

