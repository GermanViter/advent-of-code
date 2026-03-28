safeCount = 0

def isGoodDiff(arr):
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) not in [1, 2, 3]:
            return  False
    return True

def isInGoodOrder(arr):
    isIncreasing = False
    isDecreasing = False

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return False
        if arr[i] - arr[i + 1] < 0:
            isIncreasing = True
        if arr[i] - arr[i + 1] > 0:
            isDecreasing = True

    if isDecreasing and isIncreasing:
        return False
    return True

def isSafeReport(arr):
    if  isGoodDiff(arr) and isInGoodOrder(arr):
        return True

    for i in range(len(arr)):
        popedValue = arr.pop(i)
        if isGoodDiff(arr) and isInGoodOrder(arr):
            return True
        arr.insert(i, popedValue)

    return False

with open("day2.txt", "r") as file:
    for line in file:
        line = line.strip().split(' ')
        line = [int(i) for i in line]
        print(line)
        if isSafeReport(line):
            safeCount += 1
print(safeCount)
