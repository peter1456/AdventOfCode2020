from utils import read_split_line_input
from math import ceil, floor
from typing import List

boarding_pass_list = read_split_line_input(5, list)

def get_row(code: List[str]):
    low = 0
    high = 127
    for char in code:
        mid = (low + high) / 2
        if char == "F":
            high = floor(mid)
        else:
            low = ceil(mid)
    return low

def get_column(code: List[str]):
    low = 0
    high = 7
    for char in code:
        mid = (low + high) / 2
        if char == "L":
            high = floor(mid)
        else:
            low = ceil(mid)
    return low

print(max(get_row(boarding_pass[:-3]) * 8 + get_column(boarding_pass[-3:]) for boarding_pass in boarding_pass_list))