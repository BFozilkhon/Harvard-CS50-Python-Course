str: str = 'WEbBrain'

newStr: any = '' 

for i in list(str):
    if i == i.capitalize():
        newStr += i

print(newStr)