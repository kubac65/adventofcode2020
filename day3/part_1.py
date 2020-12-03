with open("day3/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

line_len = len(lines[0])
line_count = len(lines)


def calculate_trees(slope):
    left, down = slope

    x = 0
    y = 0
    trees_hit = 0

    while True:
        x += left
        y += down

        if y >= line_count:
            print(f"Finished slope {trees_hit}")
            break

        index = x % line_len

        if lines[y][index] == "#":
            trees_hit += 1

    return trees_hit


slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

result = 1
for slope in slopes:
    trees_hit = calculate_trees(slope)
    result *= trees_hit

print(result)