with open("day5/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]


def to_bit(letter):
    if letter in ["B", "R"]:
        return 1
    return 0


highest_possible_seat = (123 * 8) + 7
possible_seats = set(range(highest_possible_seat + 1))

for line in lines:
    row = int("".join([str(to_bit(letter)) for letter in line[:7]]), 2)
    col = int("".join([str(to_bit(letter)) for letter in line[7:]]), 2)
    print(f"{row=} {col=}")

    seat = (row * 8) + col
    possible_seats.remove(seat)

print(possible_seats)
