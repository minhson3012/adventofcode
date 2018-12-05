finalFreq = 0

f = open("day1input.txt", "r")
for line in f:
    value = int(line[1:])
    if '+' in line:
        finalFreq += value
    else: 
        finalFreq -= value
print(finalFreq)