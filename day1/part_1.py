with open("day1/part_1_input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

for index, number in enumerate(numbers):
    if (index) == len(numbers):
        print("didn't find a match")
        break
    for other_number in numbers[(index + 1) :]:
        if number + other_number == 2020:
            print(f"Result: {number * other_number}")
            break
