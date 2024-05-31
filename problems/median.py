num: str = "345678"

result = ''

index: int = round(len(num) / 2)

if len(num) % 2 != 0:
    result = num[index]
else:
    result = (int(num[index]) + int(num[index -1])) / 2

print(result)