def twoSum(arr, target):
    i: int = 0
    indexArr: list = list()
    while i < len(arr):
        j: int = i + 1
        while j < len(arr):
            if (arr[i] + arr[j]) == target:
                indexArr.append([i,j])
            j += 1
        i += 1

    return indexArr

    

print(twoSum([2, 7, 11,7, 15], 9))