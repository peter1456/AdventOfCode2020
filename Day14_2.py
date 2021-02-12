import re
from utils import read_split_line_input
from itertools import product

inputs = read_split_line_input(14)

mem = {}
mask = 36 * "X"
mem_re = re.compile(r"mem\[(?P<mem_loc>\d+)\] = (?P<val>\d+)")

def get_masked_locs(loc):
    bin_loc = bin(loc)[2:] # remove '0b' in front
    bin_loc = '0' * (36 - len(bin_loc)) + bin_loc
    masked_bin = ''.join(pair[1] if pair[0] == "0" else pair[0] for pair in zip(mask, bin_loc))
    x_count = masked_bin.count("X")
    masked_bin = masked_bin.replace("X", "{}")
    return map(lambda x: masked_bin.format(*x), product(("0", "1"), repeat=x_count))

for line in inputs:
    if line.startswith("mem"):
        parsed_line = mem_re.match(line).groupdict()
        for loc in get_masked_locs(int(parsed_line["mem_loc"])):
            mem[int(loc, 2)] = int(parsed_line["val"])
    else:
        mask = line.replace("mask = ", "")

print(sum(mem.values()))
