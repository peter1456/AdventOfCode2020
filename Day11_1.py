from utils import read_grid_input
from collections import Counter
from itertools import chain

original_grid = read_grid_input(11)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]

def index_in_range(x, y):
    x_in_range = 0 <= x < len(original_grid)
    y_in_range = 0 <= y < len(original_grid[0])
    return x_in_range and y_in_range

def get_adjacent_list(grid, x, y):
    adj_list = []
    for dir in dirs:
        idx_x = x + dir[0]
        idx_y = y + dir[1]
        if index_in_range(idx_x, idx_y):
            adj_list.append(grid[idx_x][idx_y])
    return adj_list

def get_next_state(grid, x, y):
    val = grid[x][y]
    if val == ".":
        return "."
    else:
        adj_list = get_adjacent_list(grid, x, y)
        if val == "L":
            if any(pos == "#" for pos in adj_list):
                return "L"
            else:
                return "#"
        else:
            if Counter(adj_list)["#"] >= 4:
                return "L"
            return "#"

def get_next_grid(grid):
    return [[get_next_state(grid, i, j) for j in range(len(grid[0]))] for i in range(len(grid))]

def check_if_eq(grid1, grid2):
    grid1_flatten = chain.from_iterable(grid1)
    grid2_flatten = chain.from_iterable(grid2)
    return all(x[0] == x[1] for x in zip(grid1_flatten, grid2_flatten))

def print_grid(grid):
    print('\n'.join(''.join(grid[i]) for i in range(len(grid))) + '\n')


grid_old, grid_new = original_grid, get_next_grid(original_grid)

while not check_if_eq(grid_old, grid_new):
    grid_old, grid_new = grid_new, get_next_grid(grid_new)

print(Counter(chain.from_iterable(grid_new))["#"])