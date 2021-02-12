from typing import Tuple
from utils import read_split_line_input
import numpy as np
from itertools import chain

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

grid = np.zeros((400, 400), dtype=bool)

for tile_expr in input_tiles:
    tile_coor = decode_tile_expr(tile_expr)
    grid[tile_coor] = 1 - grid[tile_coor]

def get_neighbourhood(coor):
    np_coor = np.array(coor)
    return [tuple((np_coor + dirs[direction]) % grid.shape[0]) for direction in dirs]

def get_black_tile_counts(grid: np.ndarray, coor: Tuple[int]):
    return sum(grid[coor] for coor in get_neighbourhood(coor))

def evolute(grid: np.ndarray):
    new_grid = grid.copy()
    black_tiles = [tuple(coor) for coor in np.argwhere(grid)]
    black_tile_neighbours = set(chain.from_iterable(get_neighbourhood(coor) for coor in black_tiles))
    for coor in black_tile_neighbours | set(black_tiles):
        black_tile_counts = get_black_tile_counts(grid, coor)
        if grid[coor]:
            new_grid[coor] = 0 < black_tile_counts < 3
        else:
            new_grid[coor] = black_tile_counts == 2
    return new_grid

for i in range(100):
    grid = evolute(grid)

print(grid.sum())
