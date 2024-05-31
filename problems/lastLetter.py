# return True if str's last letter is any forms of l

str: str = '  FoziL  '

formattedStr = str.strip().lower().endswith('l')

print(formattedStr)