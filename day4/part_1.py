with open("day4/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

expected_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

valid_pasports = 0
current_passport = set()
for line in lines:
    if line == "":
        diff = expected_fields - current_passport
        if len(diff) == 0:
            valid_pasports += 1
            print("PASS")
        elif diff == {"cid"}:
            valid_pasports += 1
            print("NORTH")
        else:
            print(f"DIFF {expected_fields - current_passport} {current_passport=}")
        current_passport = set()
        continue

    fields = line.split(" ")
    for field in fields:
        name, _ = field.split(":")
        current_passport.add(name)

print(valid_pasports)