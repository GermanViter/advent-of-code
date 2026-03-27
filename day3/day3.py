with open("day3.txt", "r") as file:
    res = 0
    for line in file:
        line = line.strip()
        numList = [int(digit) for digit in line]
        print(numList)
        result = []
        start = 0
        for i in range(12):
            end = len(numList) - 11 + i
            best = max(numList[start:end])
            best_idx = numList.index(best, start)
            result.append(best)
            start = best_idx + 1

        joltage = int(''.join(map(str, result)))
        print(joltage)
        res += joltage
    print(res)
