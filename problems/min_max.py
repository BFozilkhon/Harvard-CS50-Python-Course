numSet: list = [1,2,10,5,6,9]

firstIndex = numSet[0]

for i in numSet:
    if firstIndex < i:
        firstIndex = i

print(firstIndex)