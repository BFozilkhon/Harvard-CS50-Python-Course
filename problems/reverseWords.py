def reverseWords(txt):
    newArr = txt.split(' ')[::-1]

    return newArr

print(reverseWords('Hello Worlds'))