import re
from utils import read_split_line_input

inputs = read_split_line_input(14)

mem = {}
mask = 36 * "X"
mem_re = re.compile(r"mem\[(?P<mem_loc>\d+)\] = (?P<val>\d+)")

def get_masked_num(num):
    bin_num = bin(num)[2:] # remove '0b' in front
    bin_num = '0' * (36 - len(bin_num)) + bin_num
    masked_bin = ''.join(pair[1] if pair[0] == "X" else pair[0] for pair in zip(mask, bin_num))
    print(masked_bin)
    return int(masked_bin, 2)

for line in inputs:
    if line.startswith("mem"):
        parsed_line = mem_re.match(line).groupdict()
        mem[int(parsed_line["mem_loc"])] = get_masked_num(int(parsed_line["val"]))
    else:
        mask = line.replace("mask = ", "")
        print(mask)

print(sum(mem.values()))
