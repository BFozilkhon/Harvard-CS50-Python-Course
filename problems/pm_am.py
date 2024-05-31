# change PM AM formatted hours to 24hours format

str: str = '10:15PM'

formattedStr = str.rstrip().upper()

newStr = ''

if formattedStr.endswith('PM'):
    pmHour = int(str[0:2]) + 12
    newStr = f"{pmHour}:{str[2:5]}"
else:
    newStr = str[0,5]

print(newStr)