import regex

with open("day4/input.txt") as file:
    lines = [l.strip() for l in file.readlines()]

expected_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

hcl_regex = regex.compile(r"^#[0-9a-f]{6}\b")
ecl_allowed_values = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

pid_regex = regex.compile(r"^[0-9]{9}\b")


def byr_validator(value):
    return len(value) == 4 and (1920 <= int(value) <= 2002)


def iyr_validator(value):
    return len(value) == 4 and (2010 <= int(value) <= 2020)


def hgt_validator(value):
    try:
        unit = value[-2:]
        value = int(value[:-2])
        if unit == "cm" and (150 <= int(value) <= 193):
            return True
        if unit == "in" and (59 <= int(value) <= 76):
            return True
        return False
    except:
        return False


def hcl_validator(value):
    return hcl_regex.match(value)


def ecl_validator(value):
    return value in ecl_allowed_values


def eyr_validator(value):
    return len(value) == 4 and (2020 <= int(value) <= 2030)


def pid_validator(value):
    return pid_regex.match(value)


validators = {
    "byr": byr_validator,
    "iyr": iyr_validator,
    "eyr": eyr_validator,
    "hgt": hgt_validator,
    "hcl": hcl_validator,
    "ecl": ecl_validator,
    "pid": pid_validator,
}

valid_pasports = 0
current_passport = {}
for line in lines:
    if line == "":
        diff = expected_fields - current_passport.keys()
        if len(diff) > 0:
            # print(f"Fail fields missing {diff=}")
            current_passport = {}
            continue

        for key in current_passport:
            if key not in validators:
                continue
            if not validators[key](current_passport[key]):
                # print(f"validation failed {key=}, {current_passport[key]=}")
                break
        else:
            print(f"{current_passport} {len(current_passport)}")
            valid_pasports += 1
        current_passport = {}
    else:
        fields = line.split(" ")
        for field in fields:
            name, value = field.split(":")
            current_passport[name] = value

print(valid_pasports)