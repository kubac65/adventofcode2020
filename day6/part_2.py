with open("day6/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

total = 0
group_overlap = None
for line in lines:
    if line == "":
        total += len(group_overlap)
        group_overlap = None
        continue

    person_answers = set(h for h in line)

    if group_overlap is None:
        group_overlap = person_answers
    else:
        group_overlap = group_overlap.intersection(person_answers)

print(total)