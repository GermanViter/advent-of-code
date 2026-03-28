ranges = []
with open("day5.txt", "r") as file:
    for line in file:
        ranges.append(line.strip())
        if line.strip() == "":
            break
ranges.pop(-1)

ranges_list = sorted([(int(r.split("-")[0]), int(r.split("-")[1])) for r in ranges])

total = 0
merged_start, merged_end = ranges_list[0]
for start, end in ranges_list[1:]:
    if start <= merged_end + 1:
        merged_end = max(merged_end, end)
    else:
        total += merged_end - merged_start + 1
        merged_start, merged_end = start, end
total += merged_end - merged_start + 1

print(total)
