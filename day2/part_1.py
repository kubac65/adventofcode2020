import regex

with open("day2/input.txt") as file:
    passwords = file.readlines()

r = regex.compile(r"^(\d*)-(\d*) ([a-z]): (\w*)")

valid = 0
for password in passwords:
    min_count, max_count, letter, password = r.search(password).groups()

    count = password.count(letter)
    if int(max_count) >= count >= int(min_count):
        valid += 1

print(valid)