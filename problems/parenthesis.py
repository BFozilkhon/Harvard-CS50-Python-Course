str: str = '#fozil#web#brain#'

if str.count('#') % 2 != 0:
    raise ValueError('# must be EVEN! Missing needed character')
else: 
    count: int = 1
    newStr = ''
    for i in list(str):
        if i == '#':
            if count % 2 != 0:
                newStr += '('
            else:
                newStr += ')'
            count += 1
        else: 
            newStr += i

print(newStr)