# input: str = 'AAABBCCCA'
# output: A3B2C3A

str = 'AAABBCCCA'
count = 1

arr = list(str)
newStr = ''

for i in range(len(arr)):
    if arr[i] == arr[i+1]:
        count += 1
    else: 
        newStr += f"{arr[i]}{count}"
        count = 1

print(newStr)