from utils import read_grid_input
import numpy as np

CYCLES = 6
NEIGHBOURHOOD_4D = np.ones((3, 3, 3, 3), dtype=np.short)
NEIGHBOURHOOD_4D[1, 1, 1, 1] = 0  # center is the actual element


def add_neighbourhood_matrix(neighbourhood_matrix, coor):
    neighbourhood_matrix[coor[0] - 1:coor[0] + 2, coor[1] -
                         1:coor[1] + 2, coor[2] - 1:coor[2] + 2, coor[3] - 1:coor[3] + 2] += NEIGHBOURHOOD_4D


def get_next_state(state, neighbourhood_val):
    if state == 1:
        return 1 if 2 <= neighbourhood_val <= 3 else 0
    else:
        return 1 if neighbourhood_val == 3 else 0

get_next_state_vec = np.vectorize(get_next_state)

def evolute(state):
    neighbourhood_matrix = np.zeros_like(state)
    for coor in np.argwhere(state == 1).tolist():
        add_neighbourhood_matrix(neighbourhood_matrix, coor)
    return get_next_state_vec(state, neighbourhood_matrix)


input_grid = np.where(np.array(read_grid_input(17)) == "#", 1, 0)
initial_state = np.reshape(input_grid, (input_grid.shape[0], input_grid.shape[1], 1, 1))
initial_state = np.pad(initial_state, (CYCLES, CYCLES))

state = initial_state
for _ in range(6):
    state = evolute(state)

print(np.count_nonzero(state))