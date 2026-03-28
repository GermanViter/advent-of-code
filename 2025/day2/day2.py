def diviseurs(n):
    return [i for i in range(1, n) if n % i == 0]




def allAreEqual(array):
    compVal = array[0]

    for el in array:
        if el != compVal:
            return False
    
    return True

def isInvalidId(array):
    if len(array) == 1:
        return False
    
    if allAreEqual(array):
        return True
    else:
        for div in diviseurs(len(array)):
            result = [array[i:i+div] for i in range(0, len(array), div)]
            if not allAreEqual(result):
                continue
            return True
        return False


with open("day2.txt", "r") as file:
    ranges = []

    res = 0
    for line in file:
        ranges = line.strip().split(',')

    for rng in ranges:
        start = rng.strip().split('-')[0]
        end = rng.strip().split('-')[1]
        
        for i in range(int(start),int(end) + 1):
            numberToArray = [int(digit) for digit in str(i)]
            if isInvalidId(numberToArray):
                res += i
    print(res)






