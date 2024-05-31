birliklar: list = ["bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
onliklar: list = ["o'n", "yigirma", "o'ttiz", "qiriq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]

numericSet: list = [onliklar, birliklar]

numSet: list = list(input("Enter your number "))

count: int = 0
newStr: str = ''

for i in numSet:
    newStr += numericSet[count][int(i) - 1] + ' '
    count += 1

print(newStr)