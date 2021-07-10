import re
from utils import read_split_line_input
from pprint import pprint

input_lines = read_split_line_input(7)

line_parse_re = re.compile(r"(?P<bag_color_ext>\w+ \w+) bags contain (?P<bag_colors_int>\d \w+ \w+ bags?(, \d \w+ \w+ bags?)*)")

color_bag_graph = {}

def to_graph(line: str):
    if line.endswith("contain no other bags."):
        return
    bags_matched = line_parse_re.match(line)
    if bags_matched is None:
        return
    else:
        bags_dict = bags_matched.groupdict()
    bag_colors_int = [(int(phrase.split(" ")[0]), " ".join(phrase.split(" ")[1:3])) for phrase in bags_dict["bag_colors_int"].split(', ')]
    color_bag_graph[bags_dict["bag_color_ext"]] = bag_colors_int

for line in input_lines:
    to_graph(line)

def compute_bags_needed(color):
    if color not in color_bag_graph:
        return 0
    return sum(bag_count for bag_count, _ in color_bag_graph[color]) + sum(bag_count * compute_bags_needed(bag_color) for bag_count, bag_color in color_bag_graph[color])

print(compute_bags_needed("shiny gold"))