from utils import read_grid_input
from typing import List
from functools import reduce

input_map = read_grid_input(3)

def traverse(pos: List[int], slope_x: int, slope_y: int):
    pos[1] = (pos[1] + slope_x) % len(input_map[0])
    pos[0] += slope_y

def hit_tree(pos: List[int]):
    return input_map[pos[0]][pos[1]] == '#'

def count_hit_trees(slope_x: int, slope_y: int):
    hit_tree_count = 0
    pos = [0, 0]    

    while pos[0] < len(input_map):
        hit_tree_count += 1 if hit_tree(pos) else 0
        traverse(pos, slope_x, slope_y)

    return hit_tree_count

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

print(reduce(lambda x, y: x * y, (count_hit_trees(*slope) for slope in slopes)))