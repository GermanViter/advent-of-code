import re


sum = 0

with open("day3.txt", "r") as file:
    isAllowdToMultiply = True
    for line in file:
        multiplications = re.findall(r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)", line)
        for multiplication in multiplications:
            print(multiplication)
            if multiplication == "don't()":
                isAllowdToMultiply = False
            elif multiplication == "do()":
                isAllowdToMultiply = True
            else:
                if isAllowdToMultiply:
                    numbers = re.findall("[0-9]+", multiplication)
                    if len(numbers) != 0:
                        sum += int(numbers[0]) * int(numbers[1])
                        print(numbers)

print(sum)

