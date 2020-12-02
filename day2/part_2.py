import regex

with open("day2/input.txt") as file:
    passwords = file.readlines()

r = regex.compile(r"^(\d*)-(\d*) ([a-z]): (\w*)")

valid = 0
for password in passwords:
    index1, index2, letter, password = r.search(password).groups()

    index1_letter = password[int(index1) - 1]
    index2_letter = password[int(index2) - 1]
    if (index1_letter == letter) != (index2_letter == letter):
        valid += 1

print(valid)