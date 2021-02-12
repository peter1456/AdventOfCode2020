from utils import read_grid_input
import numpy as np

original_grid = np.array(read_grid_input(11))

def rectangular_diag(diag, k, shape):
    rect_diag = np.zeros(shape, dtype=int)
    square_diag = np.diag(diag)
    if k < 0:
        rect_diag[-k:-k+len(diag),0:len(diag)] += square_diag
    else:
        rect_diag[0:len(diag),k:k+len(diag)] += square_diag
    return rect_diag

def is_first_seat_occupied(arr, reverse):
    if "L" not in arr and "#" not in arr:
        return False
    if reverse:
        first_seat_idx = arr.shape[0] - np.argmax(np.flip(arr) != ".") - 1
    else:
        first_seat_idx = np.argmax(arr != ".")
    return arr[first_seat_idx] == "#"
    

def get_adjacent_row(row):
    adjacent_row = np.zeros_like(row, dtype=int)
    for i in range(row.shape[0] - 1):
        # Left Direction
        adjacent_row[i] += is_first_seat_occupied(row[i + 1:], reverse=False)
    for i in range(1, row.shape[0]):
        # Right Direction
        adjacent_row[i] += is_first_seat_occupied(row[:i], reverse=True)
    return adjacent_row


def get_adjacent_matrix(grid):
    adj_matrix = np.zeros(grid.shape, dtype=int)

    # left and right
    for i in range(grid.shape[0]):
        adj_matrix[i,:] += get_adjacent_row(grid[i,:]) 

    # up and down
    for i in range(grid.shape[1]):
        adj_matrix[:,i] += get_adjacent_row(grid[:,i])

    # diagonal
    for k in range(-grid.shape[0] + 1, grid.shape[1]):
        diag = np.diagonal(grid, offset=k)
        adj_matrix += rectangular_diag(get_adjacent_row(diag), k, grid.shape)
    
    # anti-diagonal
    for k in range(-grid.shape[0] + 1, grid.shape[1]):
        diag = np.diagonal(np.fliplr(grid), offset=k)
        adj_matrix += np.fliplr(rectangular_diag(get_adjacent_row(diag), k, grid.shape))

    return adj_matrix

def get_next_state(grid, adj_matrix, x, y):
    val = grid[x][y]
    if val == ".":
        return "."
    else:
        if val == "L":
            return "L" if adj_matrix[x][y] > 0 else "#"
        else:
            return "L" if adj_matrix[x][y] >= 5 else "#"

def get_next_grid(grid):
    adj_matrix = get_adjacent_matrix(grid)
    return np.array([[get_next_state(grid, adj_matrix, i, j) for j in range(len(grid[0]))] for i in range(len(grid))])

def print_grid(grid):
    print('\n'.join(''.join(str(grid.tolist()[i])) for i in range(len(grid))) + '\n')

grid_old, grid_new = original_grid, get_next_grid(original_grid)

while not np.array_equal(grid_old, grid_new):
    grid_old, grid_new = grid_new, get_next_grid(grid_new)
print(np.count_nonzero(grid_new == "#"))