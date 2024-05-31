#first
tr: str = 'fozil'

newStr = ''

for i in list(str):
    newStr = i + newStr

print(newStr)

#second
num: int = 12121

str: str = str(num)[::-1]

print(int(str) == num)
