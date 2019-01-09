while(True):
    dim = input()
    x,y = map(int,dim.split())
    if(x ==0 or y == 0):
        break
    cordinates = input()
    poses = [] 
    total = 0
    poses = list(map(int,cordinates.split()))
    atual = 0 
    anterior = x

    for i in poses:

        atual = i
        
        if atual < anterior:
            total += (anterior-atual)
        
        anterior = atual

    print(total)
