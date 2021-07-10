import re
from utils import read_split_line_input
from functools import reduce

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
    bag_colors_int = [' '.join(phrase.split(' ')[1:3]) for phrase in bags_dict["bag_colors_int"].split(', ')]
    for color in bag_colors_int:
        if color in color_bag_graph:
            color_bag_graph[color].append(bags_dict["bag_color_ext"])
        else:
            color_bag_graph[color] = [bags_dict["bag_color_ext"]]

for line in input_lines:
    to_graph(line)

def find_upstream_colors(color):
    if color not in color_bag_graph:
        return set()
    return set(color_bag_graph[color]) | reduce(lambda x, y: x | y, (find_upstream_colors(color_up) for color_up in color_bag_graph[color]))

print(len(set(find_upstream_colors("shiny gold"))))