from os import read
from utils import read_raw_input

passports = read_raw_input(4).split("\n\n")

EXPECTED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

def get_passport_field_names(passport: str):
    one_line_passport = passport.replace("\n", " ")
    field_names = [field.split(":")[0] for field in one_line_passport.split(" ")]
    print(field_names)
    return field_names

def check_valid_passport(passport: str):
    field_names = get_passport_field_names(passport)
    if "cid" in field_names:
        field_names.remove("cid")
    return set(field_names) == EXPECTED_FIELDS

print(len(list(filter(check_valid_passport, passports))))