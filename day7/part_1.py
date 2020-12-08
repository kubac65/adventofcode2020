rules = {}
with open("day7/input.txt") as file:
    for line in file:
        outer_color, inners = line.split("contain")
        outer_color = " ".join(outer_color.split(" ")[:2])
        if inners.strip() == "no other bags.":
            continue

        inner_bags = inners.strip().split(",")
        for inner in inner_bags:
            split = inner.strip().split(" ")
            color = " ".join(split[1:3])
            if color not in rules:
                rules[color] = set()
            rules[color].add(outer_color)


def find_all_containing_bags(color="shiny gold", result=set()):
    if color not in rules:
        return result

    colors = rules[color]
    result.update(colors)
    for color in colors:
        find_all_containing_bags(color, result)
    return result


print(rules)
result = find_all_containing_bags()
print(f"{result=} {len(result)=}")
