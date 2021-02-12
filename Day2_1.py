import re
from utils import read_split_line_input
from collections import Counter

inputs = read_split_line_input(2)

policy_re = re.compile(r"(?P<lower_bd>\d{1,2})-(?P<upper_bd>\d{1,2}) (?P<policy_char>\w)")

def decode_policy(policy):
    return policy_re.match(policy).groupdict()

def check_valid_password(policy, password):
    decoded_policy = decode_policy(policy)
    password_counter = Counter(password)
    return int(decoded_policy["lower_bd"]) <= password_counter[decoded_policy["policy_char"]] <= int(decoded_policy["upper_bd"])

def check_valid_line(line):
    policy, password = line.split(': ')
    return check_valid_password(policy, password)

print(len(list(filter(check_valid_line, inputs))))