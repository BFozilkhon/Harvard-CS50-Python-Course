# 3ga bo'linadi, 5ga bo'linadi, 3ga va 5ga bo'linadi

num: int = int(input('Enter your number '))

if num % 3 == 0 and num % 5 == 0:
    print("3ga va 5ga bo'linadi")
elif num % 3 == 0:
    print("3ga bo'linadi")
elif num % 5 == 0:
    print("5ga bo'linadi")