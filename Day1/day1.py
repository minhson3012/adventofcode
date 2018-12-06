currentFreq = 0
totalFreq = []
duplicateFreq = 0
duplicateFound = False

f = open("day1input.txt", "r")
lines = f.readlines()
f.close()

while True:
    for line in lines:
        value = int(line[1:])
        sign = line[0]
        if sign == '+':
            currentFreq += value
        else: 
            currentFreq -= value

        if currentFreq in totalFreq:
            duplicateFreq = currentFreq
            duplicateFound = not duplicateFound
            break
        else:
            totalFreq.append(currentFreq)
    if duplicateFound:
        break
print(duplicateFreq)
