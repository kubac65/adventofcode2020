from itertools import permutations
from functools import reduce

with open("day1/part_1_input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

perms = permutations(numbers, 3)

for perm in perms:
    if reduce(lambda x, y: x + y, perm) == 2020:
        print(f"Result: {reduce(lambda x, y: x * y, perm)}")
        break
