from utils import read_raw_input
import numpy as np
import re
from networkx import Graph
from networkx.algorithms import bipartite

inputs = read_raw_input(16)

ticket_fields, my_ticket, nearby_tickets = inputs.split('\n\n')

ticket_fields = ticket_fields.split("\n")

ticket_field_re = re.compile(r"(?P<min_1>\d{2,3})-(?P<max_1>\d{2,3}) or (?P<min_2>\d{2,3})-(?P<max_2>\d{2,3})")

valid_nums = np.zeros((1000,), dtype=np.bool_)
fields = {}

def parse_ticket_field(ticket_field):
    field_name, valid_ranges = ticket_field.split(": ")
    parsed_ranges = ticket_field_re.match(valid_ranges).groupdict()
    set_valid_num(parsed_ranges)
    fields[field_name] = np.zeros((1000,), dtype=np.bool_)
    fields[field_name][int(parsed_ranges["min_1"]):int(parsed_ranges["max_1"]) + 1] = 1
    fields[field_name][int(parsed_ranges["min_2"]):int(parsed_ranges["max_2"]) + 1] = 1

def set_valid_num(parsed_ranges):
    valid_nums[int(parsed_ranges["min_1"]):int(parsed_ranges["max_1"]) + 1] = 1
    valid_nums[int(parsed_ranges["min_2"]):int(parsed_ranges["max_2"]) + 1] = 1

def is_valid_ticket(ticket):
    return all(valid_nums[field_value] for field_value in ticket)

def get_ticket_field_matching(fields, tickets):
    num_tickets = tickets.shape[0]

    # initialize matching graph
    ticket_field_matching = Graph()
    ticket_field_matching.add_nodes_from(fields.keys(), bipartite=0)
    ticket_field_matching.add_nodes_from(range(tickets.shape[1]), bipartite=1)

    for field_name in fields.keys():
        field_func = np.vectorize(lambda x: fields[field_name][x])
        matched_ticket_fields = np.where(np.sum(field_func(tickets), axis=0) == num_tickets)[0]
        ticket_field_matching.add_edges_from([(field_name, ticket_field) for ticket_field in matched_ticket_fields])

    return bipartite.matching.hopcroft_karp_matching(ticket_field_matching, fields.keys())
        

for ticket_field in ticket_fields:
    parse_ticket_field(ticket_field)

nearby_tickets = nearby_tickets.split("\n")[1:]
nearby_tickets = [[int(field_value) for field_value in line.split(",")] for line in nearby_tickets]

valid_tickets = np.array(list(filter(is_valid_ticket, nearby_tickets)))

matching = get_ticket_field_matching(fields, valid_tickets)
departure_only_matching = {key: value for key, value in matching.items() if isinstance(key, str) and key.startswith("departure")}

my_ticket = my_ticket.split("\n")[1]
my_ticket = [int(field_value) for field_value in my_ticket.split(",")]

result = 1
for idx in departure_only_matching.values():
    result *= my_ticket[idx]

print(result)
