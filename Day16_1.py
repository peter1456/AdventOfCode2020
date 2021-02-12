from os import read
from utils import read_raw_input
import numpy as np
import re
from itertools import chain

inputs = read_raw_input(16)

ticket_fields, _, nearby_tickets = inputs.split('\n\n')

ticket_fields = ticket_fields.split("\n")

ticket_field_re = re.compile(r"(?P<min_1>\d{2,3})-(?P<max_1>\d{2,3}) or (?P<min_2>\d{2,3})-(?P<max_2>\d{2,3})")

valid_nums = np.zeros((1000,), dtype=np.bool_)

def set_valid_num(ticket_field):
    ticket_field = ticket_field.split(": ")[1]
    parsed_fields = ticket_field_re.match(ticket_field).groupdict()
    valid_nums[int(parsed_fields["min_1"]):int(parsed_fields["max_1"]) + 1] = 1
    valid_nums[int(parsed_fields["min_2"]):int(parsed_fields["max_2"]) + 1] = 1

for ticket_field in ticket_fields:
    set_valid_num(ticket_field)

nearby_tickets = nearby_tickets.split("\n")[1:]
nearby_tickets = [[int(ticket_no) for ticket_no in line.split(",")] for line in nearby_tickets]
nearby_tickets = chain.from_iterable(nearby_tickets)

invalid_tickets = filter(lambda x: not valid_nums[x], nearby_tickets)

print(sum(invalid_tickets))
