import re
from utils import read_raw_input

passports = read_raw_input(4).split("\n\n")

def check_height(hgt: str):
    if not (match := re.match(r"^(?P<height>\d{2,3})(?P<unit>cm|in)$", hgt)):
        return False
    hgt_detail = match.groupdict()
    if hgt_detail["unit"] == "cm":
        return 150 <= int(hgt_detail["height"]) <= 193
    else:
        return 59 <= int(hgt_detail["height"]) <= 76

EXPECTED_FIELDS = {
    "byr": lambda x: re.match(r"^\d{4}$", x) and 1920 <= int(x) <= 2002, 
    "iyr": lambda x: re.match(r"^\d{4}$", x) and 2010 <= int(x) <= 2020, 
    "eyr": lambda x: re.match(r"^\d{4}$", x) and 2020 <= int(x) <= 2030, 
    "hgt": check_height, 
    "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x), 
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], 
    "pid": lambda x: re.match(r"^\d{9}$", x)
}

def get_passport_fields(passport: str):
    one_line_passport = passport.replace("\n", " ")
    fields = {key: value for key, value in (field.split(":") for field in one_line_passport.split(" "))}
    return fields

def check_valid_passport(passport: str):
    fields = get_passport_fields(passport)
    if "cid" in fields:
        del fields["cid"]
    return set(fields.keys()) == set(EXPECTED_FIELDS.keys()) and all(EXPECTED_FIELDS[field](value) for field, value in fields.items())

print(len(list(filter(check_valid_passport, passports))))