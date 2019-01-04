vector = []

quantNumbers = int(input())
numbers = input().split(" ")
intnumbers = []

for i in numbers:
    intnumbers.append(int(i))

minimo = min(intnumbers)
print("Menor valor: " + str(minimo))
print("Posicao: " + str(intnumbers.index(minimo)))

