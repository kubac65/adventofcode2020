with open("day6/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

total = 0
group_tally = set()
for line in lines:
    if line == "":
        total += len(group_tally)
        group_tally = set()
        continue

    group_tally.update(set(h for h in line))

print(total)