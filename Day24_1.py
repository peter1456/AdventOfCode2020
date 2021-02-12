from utils import read_split_line_input
import numpy as np

input_tiles = read_split_line_input(24)

dirs = {
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
    "ne": (1, -1)
}

def split_dirs(expr: str):
    if not expr:
        return []
    for direction in dirs:
        if expr.startswith(direction):
            return [direction] + split_dirs(expr[len(direction):])

def decode_tile_expr(expr: str):
    expr_splitted = split_dirs(expr)
    tile_coor = np.zeros(2, dtype=int)
    for direction in expr_splitted:
        tile_coor += dirs[direction]
    return tuple(tile_coor)

grid = np.zeros((30, 30), dtype=bool)

for tile_expr in input_tiles:
    tile_coor = decode_tile_expr(tile_expr)
    grid[tile_coor] = 1 - grid[tile_coor]

print(grid.sum())