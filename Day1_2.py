from utils import read_split_line_input

def two_sum(num_list, target):
    low = 0
    high = len(num_list) - 1

    while (low != high and num_list[low] + num_list[high] != target):
        if num_list[low] + num_list[high] > target:
            high -= 1
        else:
            low += 1
    
    if low == high:
        return False
    return num_list[low], num_list[high]

inputs = read_split_line_input(1, int)
inputs.sort()

for num in inputs:
    two_sum_list = inputs.copy()
    two_sum_list.remove(num)
    if out := two_sum(two_sum_list, 2020 - num):
        if num + out[0] + out[1] == 2020:
            print(num * out[0] * out[1])
            break