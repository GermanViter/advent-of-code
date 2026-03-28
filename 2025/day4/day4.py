matrix = []

with open("day4.txt", "r") as file:
    for line in file:
        arr = list(line.strip())
        matrix.append(arr)


res = 0


canContinue = True
while canContinue:
    currentRes = 0
    to_remove = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '@':
                neighbours = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[ni]):
                            if matrix[ni][nj] == '@':
                                neighbours += 1
                if neighbours < 4:
                    to_remove.append((i, j))

    for i, j in to_remove:
        matrix[i][j] = '.'
    res += len(to_remove)
    currentRes = len(to_remove)
    if currentRes == 0:
        canContinue = False

print(res)
