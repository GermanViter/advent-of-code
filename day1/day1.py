import operator

currentNumber = 50
operations = {
    "R" : operator.add,
    "L" : operator.sub
}
count = 0


with open("day1.txt", "r") as file:
    for line in file:
        line = line.strip()
        number = int(line[1:])
        op = line[0]
        operation = operations[op]
 
        numberUntilZero = 0

        if op == "R":
            numberUntilZero += 100 - currentNumber
        else:
            numberUntilZero += currentNumber

        if numberUntilZero == 0:
            numberUntilZero = 100

        if number >= numberUntilZero:
            count += 1 + (number - numberUntilZero) // 100

        currentNumber = operations[op](currentNumber, number) % 100
print(count)


