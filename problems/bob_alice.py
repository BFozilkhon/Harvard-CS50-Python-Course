step: int = int(input('Enter your number '))

i = 1

while i <= step:
    if step % 2 == 0:
        print('Alice won, Bob lose')
    else: 
        print('Bob won, Alice lose')
    i += 1
