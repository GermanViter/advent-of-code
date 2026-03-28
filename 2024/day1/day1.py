left = []
rigth = []
difs = []

with open("day1.txt", "r") as file:
    for line in file:
        line = line.strip().split("   ")
        left.append(line[0])
        rigth.append(line[1])
left.sort()
rigth.sort()

count = 0

for i in rigth:
    for j in left:
        if i == j:
            count += int(i)

print(count)
