rules = {}

with open("day7/input.txt") as file:
    for line in file:
        outer_color, inners = line.split("contain")
        outer_color = " ".join(outer_color.split(" ")[:2])
        if inners.strip() == "no other bags.":
            continue

        if outer_color not in rules:
            rules[outer_color] = set()

        inner_bags = inners.strip().split(",")
        for inner in inner_bags:
            split = inner.strip().split(" ")
            color = " ".join(split[1:3])
            count = int(split[0])
            rules[outer_color].add((count, color))


def find_all_contained_bags(color="shiny gold"):
    needed_bags = 0
    if color not in rules:
        return needed_bags

    inner_bags = rules[color]

    for count, color in inner_bags:
        needed_bags += count
        needed_bags += count * find_all_contained_bags(color)

    return needed_bags


print(rules)
result = find_all_contained_bags()

print(f"{result=}")
