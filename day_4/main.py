import re
input_file = ""
with open("input", "r") as f:
    input_file = f.read()
input_file = input_file.replace("\n\n", "|||")
input_file = input_file.replace("\n", " ")

print(input_file)

processed_file = input_file.split("|||")

print(processed_file)

required_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

def is_int_range(data, min, max):
    try:
        b = int(data)
        if b < min or b > max:
            return False
    except:
        return False
    return True


def validate_data(line):
    data = re.findall("(...):(\S*)", line)

    print(data)

    for field in data:
        # print(field)
        if field[0] == "byr":
            if len(field[1]) != 4:
                print("byr bad")
                return False
            if not is_int_range(field[1], 1920, 2002):
                print("byr bad")
                return False
        elif field[0] == "iyr":
            if len(field[1]) != 4:
                print("iyr bad")
                return False
            if not is_int_range(field[1], 2010, 2020):
                print("iyr bad")
                return False
        elif field[0] == "eyr":
            if len(field[1]) != 4:
                print("eyr bad")
                return False
            if not is_int_range(field[1], 2020, 2030):
                print("eyr bad")
                return False
        elif field[0] == "hgt":
            if "cm" in field[1]:
                if not is_int_range(field[1][:-2], 150, 193):
                    print("hgt bad")
                    return False
            elif "in" in field[1]:
                if not is_int_range(field[1][:-2], 59, 76):
                    print("hgt bad")
                    return False
            else:
                print("hgt bad")
                return False
        elif field[0] == "hcl":
            if len(field[1]) != 7:
                return False
            for c in field[1][1:]:
                if c not in "abcdef0123456789":
                    return False
        elif field[0] == "ecl":
            if field[1] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif field[0] == "pid":
            if len(field[1]) != 9:
                return False
            try:
                int(field[1])
            except:
                return False
    return True

old_ic = 0
invalid_count = 0
for line in processed_file:
    matches = re.findall("(...):\S*", line)
    bad = False
    for f in required_fields:
        if f not in matches:
            bad = True
            break
    if not bad:
        if validate_data(line) == False:
            print("invalid data")
            bad = True

    if bad:
        invalid_count += 1

print(len(processed_file) - invalid_count)

