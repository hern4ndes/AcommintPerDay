a = int(input())
b = int(input())
total = 0

if (a > b):
    for i in range(b,a+1):
        if(i%13 > 0):
            total += i    
     
else:

    for i in range(a,b+1):
        if(i%13 > 0):
            total += i   
            
print (total)
    
