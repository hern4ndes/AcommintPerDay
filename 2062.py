numeros = int(input())
texto = input().split()
final = " "
for i in range(numeros):
    if(i == numeros-1):
        final = "\n"
        
    if((texto[i][0:2] in "OB") and (len(texto[i])==3) and (i < numeros)):
        print("OBI",end = final ),
    elif((texto[i][0:2] in "UR") and (len(texto[i])==3)and (i < numeros)):
        print("URI",end = final)
    elif(i < numeros):
        print(texto[i], end = final)

    
print()