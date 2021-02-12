from utils import read_grid_input
from typing import List

input_map = read_grid_input(3)

def traverse(pos: List[int], x: int, y: int):
    pos[1] = (pos[1] + x) % len(input_map[0])
    pos[0] += y

def hit_tree(pos: List[int]):
    return input_map[pos[0]][pos[1]] == '#'

tree_count = 0
pos = [0, 0]

while pos[0] < len(input_map):
    tree_count += 1 if hit_tree(pos) else 0
    traverse(pos, 3, 1)

print(tree_count)