import re
from utils import read_split_line_input

inputs = read_split_line_input(2)

policy_re = re.compile(r"(?P<first_pos>\d{1,2})-(?P<second_pos>\d{1,2}) (?P<policy_char>\w)")

def decode_policy(policy):
    return policy_re.match(policy).groupdict()

def check_valid_password(policy, password):
    decoded_policy = decode_policy(policy)
    return (password[int(decoded_policy["first_pos"]) - 1] == decoded_policy["policy_char"]) ^ (password[int(decoded_policy["second_pos"]) - 1] == decoded_policy["policy_char"])

def check_valid_line(line):
    policy, password = line.split(': ')
    return check_valid_password(policy, password)

print(len(list(filter(check_valid_line, inputs))))