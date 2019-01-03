times = int(input())

values = []
allvalues = []

for i in range(times):
    number = int(input())
    allvalues.append(number)
    if number not in values:
        values.append(number)
values.sort()
for i in values:
    print(str(i) + " aparece " + str(allvalues.count(i)) + " vez(es)")
