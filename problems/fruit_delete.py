def delete_fruit(fruitSet, target):
    newArr: list = list()
    
    for i in fruitSet:
        if target not in i:
            newArr.append(i)

    return newArr

target = input('What u wanna delete? ').strip()

print(
delete_fruit(['olma', 'nok', 'anor', 'olma', 'banan'], target)
)