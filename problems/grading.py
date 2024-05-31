grade: int = int(input('What is grade? '))

if grade <= 100 and grade >= 86:
    print('A')
elif grade < 86 and grade >= 61:
    print('B')
else: 
    print('C')