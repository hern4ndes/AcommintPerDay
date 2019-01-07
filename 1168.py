quant = int(input())

for i in range(quant):
    leds = 0
    num = str(input())
    for j in range(len(num)):
      
        if(num[j] == '1'):
            leds += 2
        elif(num[j] == '2'):
            leds += 5
        elif(num[j] == '3'): 
            leds += 5
        elif(num[j] == '4'): 
            leds += 4
        elif(num[j] == '5'):
            leds += 5
        elif(num[j] == '6'): 
            leds += 6
        elif(num[j] == '7'):
            leds += 3
        elif(num[j] == '8'):
            leds += 7
        elif(num[j] == '9'):
            leds += 6
        elif(num[j] == '0'):
            leds += 6
    print (str(leds)+ " leds")